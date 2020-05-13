from django.apps import apps
from django.core.serializers import serialize
from . import models
from django.apps import apps

part_types = ['CPU','GPU','Motherboard','Ram_set', 'PSU', 'Storage', 'Case', 'CPU_Cooler']
optional_types = ['Optical_Drive', 'Sound_Card', 'Monitor', 'Operating_System']

def configure_logic(request):
    radio_list = list()
    for name in part_types:
        radio_list.append(request.POST.get(name))
    for name in optional_types:
        post = request.POST.get(name)
        if post:
            radio_list.append(post)

    message_text = list()
    selections = [i for i in radio_list if i]
    
    parts = dict()
    for item in selections:
        values = item.split("-")
        if values[1] == "0" and values[0] not in optional_types:
            radio_list.append(None)
        if values[1] != "0":
            parts.update({ values[0]: apps.get_model('main', values[0]).objects.filter(id=values[1]).first() })

    if None in radio_list:
        message_text.append("Unselected mandatory fields")
    compat_validation(parts, message_text)

    if message_text:
        if not selections:
            selections.append("none selected")
        return [[selections, message_text]]

    configuration = models.Configuration()
    for item in selections:
        values = item.split("-")
        model = apps.get_model('main', values[0]).objects.filter(id=values[1]).first()
        exec("configuration." + values[0] + " = model")

    configuration.save()

    if request.user.is_authenticated:
        saved_build = models.Saved_build(Belongs_to_user = request.user, Configuration = configuration)
        saved_build.save()
    
    return [None, configuration.id]


def compat_validation(parts, message_text):
    if "CPU" in parts and "Motherboard" in parts:
        if not parts['CPU'].Socket == parts['Motherboard'].CPU_socket or \
         not parts['CPU'].Generation in parts['Motherboard'].Supported_CPU_generations.split("/"):
            message_text.append("CPU and Motherboard are incompatible (socket or chipset)")

    if "Case" in parts and "GPU" in parts:
        if parts['GPU'].Length > parts['Case'].Max_GPU_lenght:
            message_text.append("The GPU is too long for the selected case")

    if "Case" in parts and "CPU_Cooler" in parts:
        if float(parts['CPU_Cooler'].Dimmensions.split(" x ")[2]) >= parts['Case'].Max_CPU_Cooler_height:
            message_text.append("The CPU cooler is too tall for the selected case")

    if "Case" in parts and "Motherboard" in parts:
        if not parts['Motherboard'].Form_Factor in parts['Case'].Supported_Motherboard_Form_Factors.split(", "):
            message_text.append("Selected case does not support the motherboard form factor")

    if "Storage" in parts and "Motherboard" in parts:
        if parts['Storage'].Connection == "M.2" and parts['Motherboard'].Nr_of_mdot2_slots == 0:
            message_text.append("Selected motherboard does not support m.2 storage")
        if parts['Storage'].Connection == "SATA" and parts['Motherboard'].Nr_of_Sata_ports == 0:
            message_text.append("Selected motherboard does not support SATA storage")

    if "GPU" in parts and "PSU" in parts:
        if parts['GPU'].Recommended_System_Power > parts['PSU'].Total_Wattage:
            message_text.append("Power supply does not achieve recommended power output")
        elif "CPU" in parts:
            needed_power = parts['GPU'].Power + parts['CPU'].TDP
            needed_power = needed_power + 0.4*needed_power
            if needed_power > parts['PSU'].Total_Wattage:
                message_text.append("Power supply does not achieve recommended power output")
                
    if "Ram_set" in parts and "Motherboard" in parts:
        if parts['Ram_set'].Nr_of_Sticks > parts['Motherboard'].Nr_of_Ram_slots:
            message_text.append("Motherboard does not have enough slots for selected ram set")
    
    if "Case" in parts and "PSU" in parts:
        if not parts['PSU'].Form_Factor in parts['Case'].Supported_PSU_Form_Factor.split(", "):
            message_text.append("Selected case does not support PSU form factor")

    if "Optical_Drive" in parts and "Case" in parts:
        if not parts['Case'].Optical_Drive_support:
            message_text.append("Selected case does not support optical drives")

    if "Sound_Card" in parts and "Motherboard" in parts:
        if (parts['Motherboard'].Nr_of_PCIe_x16_slots + parts['Motherboard'].Nr_of_PCIe_x4_slots + parts['Motherboard'].Nr_of_PCIe_x1_slots) < 2:
            message_text.append("Selected motherboard does not have enough PCI Express connection to support a sound card")


def get_saved_builds(user):
    saved_builds = apps.get_model('main','Saved_build').objects.filter(Belongs_to_user=user)
    saved_ser = serialize("python", saved_builds)
    conf_ser = []
    names = []
    for item in saved_ser:
        names.append(item['fields']['Name'])

    for item in saved_ser:
        conf = apps.get_model('main','Configuration').objects.filter(id = item['fields']['Configuration'])
        conf_ser += serialize("python", conf)

    builds = list()
    for i in range(0,len(conf_ser)):
        del conf_ser[i]['fields']['Date_Saved']
        temp = list()
        sum = 0
        for key, value in conf_ser[i]['fields'].items():
            if value:
                part = apps.get_model('main', key).objects.filter(id=value).first()
                temp.append(part)
                sum = sum + float(part.Price)
        sum = round(sum, 2)
        builds.append({'name':names[i], 'parts': temp, 'total': sum, 'confID': conf_ser[i]['pk']})

    return (builds, conf_ser)

