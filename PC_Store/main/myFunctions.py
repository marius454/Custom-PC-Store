from django.apps import apps
from django.core.serializers import serialize
from . import models

part_types = ['CPU','GPU','Motherboard','Ram_set', 'PSU', 'Storage', 'Case', 'CPU_Cooler']

def configure_logic(request):
    radio_list = list()
    for name in part_types:
        radio_list.append(request.POST.get(name))

    message_text = list()
    selections = [i for i in radio_list if i]
    
    parts = dict()
    for item in selections:
        values = item.split("-")
        parts.update({ values[0]: apps.get_model('main', values[0]).objects.filter(id=values[1]).first() })

    if None in radio_list:
        message_text.append("Unselected fields")
    compat_validation(parts, message_text)

    if message_text:
        if not selections:
            selections.append("none selected")
        return [selections, message_text]

    configuration = models.Configuration(UserID = request.user)
    for item in selections:
        values = item.split("-")
        exec("configuration." + values[0] + " = apps.get_model('main', values[0]).objects.filter(id=values[1]).first()")

    # configuration.save()
    return None

def compat_validation(parts, message_text):
    if "CPU" in parts and "Motherboard" in parts:
        if not parts['CPU'].Socket == parts['Motherboard'].CPU_socket or \
         not parts['CPU'].Generation in parts['Motherboard'].Supported_CPU_generations.split("/"):
            message_text.append("CPU and Motherboard are incompatible (socket or chipset)")

    if "Case" in parts and "GPU" in parts:
        if parts['GPU'].Length > parts['Case'].Max_GPU_lenght:
            message_text.append("The GPU is too long for the selected case")

    if "Case" in parts and "CPU_Cooler" in parts:
        if parts['CPU_Cooler'].Dimmensions.split(" x ")[2] >= parts['Case'].Max_CPU_Cooler_height:
            message_text.append("The CPU cooler is too tall for the selected case")

    if "Case" in parts and "Motherboard" in parts:
        if not parts['Motherboard'].Form_Factor in parts['Case'].Supported_Motherboard_Form_Factors:
            message_text.append("Selected case does not support the motherboard form factor")

    if "Storage" in parts and "Motherboard" in parts:
        if parts['Storage'].Connection == "M.2" and parts['Motherboard'].Nr_of_mdot2_slots == 0:
            message_text.append("Selected motherboard does not support m.2 storage")
        if parts['Storage'].Connection == "SATA" and parts['Motherboard'].Nr_of_Sata_slots == 0:
            message_text.append("Selected motherboard does not support SATA storage")

    if "GPU" in parts and "PSU" in parts:
        if parts['GPU'].Recommended_System_Power > parts['PSU'].Total_Wattage:
            message_text.append("Power supply does not achieve rocommended power output")
        elif "CPU" in parts:
            needed_power = parts['GPU'].Power + parts['CPU'].TDP
            needed_power = needed_power + 0.4*needed_power
            if needed_power > parts['PSU'].Total_Wattage:
                message_text.append("Power supply does not achieve rocommended power output")
                
    if "Ram_set" in parts and "Motherboard" in parts:
        if parts['Ram_set'].Nr_of_Sticks > parts['Motherboard'].Nr_of_Ram_slots:
            message_text.append("Motherboard does not have enough slots for selected ram set")
    

