from django.shortcuts import render
from .models import Order, Payment_Info
from django.apps import apps
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from .forms import CheckoutForm, PaymentForm
from django.core.mail import send_mail
import os
from main import myFunctions as mf
from django.contrib.auth.decorators import login_required


def CartView(request, confID):
    savedText = request.GET.get('saved')
    saved = False
    if savedText == 'True':
        saved = True
    
    conf = apps.get_model('main','Configuration').objects.filter(id = confID)
    conf_ser = serialize("python", conf)
    build = list()
    del conf_ser[0]['fields']['Date_Saved']
    sum = 0
    for key, value in conf_ser[0]['fields'].items():
        if value:
            part = apps.get_model('main', key).objects.filter(id=value).first()
            build.append(part)
            sum = sum + float(part.Price)
    sum = round(sum, 2)
    build.append(sum)

    if request.POST:

        return HttpResponseRedirect(reverse('checkout', kwargs={'confID': confID}))

    context= {
        'title': "Shopping Cart",
        'build': build,
        'saved': saved
    }
    return render(request, "orders/cart.html", context)

def Checkout(request, confID):
    conf = apps.get_model('main','Configuration').objects.filter(id = confID)
    conf_ser = serialize("python", conf)
    del conf_ser[0]['fields']['Date_Saved']
    sum = 0
    for key, value in conf_ser[0]['fields'].items():
        if value:
            part = apps.get_model('main', key).objects.filter(id=value).first()
            sum = sum + float(part.Price)
    sum = round(sum, 2)

    shipping_total = 0.00
    if sum < 1500:
        shipping_total = 20.00

    user = request.user
    payment = None
    
    
    c_form = CheckoutForm(request.POST or None)
    p_form = PaymentForm(request.POST or None)
    if user.is_authenticated:
        payment = Payment_Info.objects.filter(user = user).first()
        p_form = PaymentForm(request.POST or None, instance = payment)

    if c_form.is_valid() and p_form.is_valid():
        c_instance = c_form.save(commit=False)
        c_instance.sub_total = sum
        c_instance.shipping_cost = shipping_total
        c_instance.final_total = sum + shipping_total
        c_instance.configuration = conf.first()

        if user.is_authenticated:
            c_instance.user = user
            c_instance.save()
            p_instance = p_form.save(commit=False)
            p_instance.user = user
            p_instance.save()
        else:
            c_instance.user = None
            c_instance.save()
        
        email_body = "Thank you for ordering a computer from my store. This is a conformation email of a successful order for a configuration with the parts: \n"
        for key, value in conf_ser[0]['fields'].items():
            if value:
                part = apps.get_model('main', key).objects.filter(id=value).first()
                email_body += "\t" + part.Brand + " " + part.Name + " - " + str(part.Price) + "€\n"
        email_body += "\ttotal - " + str(sum) + "€\n"
        email_body += "\nThank you for your support. \nPC Store"
        send_mail("Order confirmation from PC Store", email_body, os.environ.get('EMAIL_USER'), [c_instance.email])

        return render(request, 'orders/checkout_complete.html')

    if user.is_authenticated:
        c_form = CheckoutForm(initial={
            'recipient_first_name': user.first_name, 
            'recipient_last_name': user.last_name,
            'email': user.email,
            'phone': user.profile.Phone,
            'country': user.profile.Country,
            'delivery_address': user.profile.Delivery_Address,
            })

        if payment:
            p_form = PaymentForm(instance = payment)

    context={
        'c_form': c_form,
        'p_form': p_form,
        'sub_total': sum,
        'shipping_total': round(shipping_total, 2),
        'final_total': sum + shipping_total,
    }
    return render(request, "orders/checkout.html", context)

@login_required
def OrderView (request):
    get_orders = apps.get_model('orders','Order').objects.filter(user = request.user)
    orders_ser = serialize("python", get_orders)
    id_list = []
    for item in orders_ser:
        id_list.append(item['fields']['configuration'])

    print(id_list)

    builds, conf_ser = mf.get_saved_builds(request.user)
    if builds:
        i = 0
        n = len(builds)
        while i < n:
            if builds[i]['confID'] not in id_list:
                del builds[i]
                n -= 1
            else:
                i += 1
    
    for i in range(0, len(orders_ser)):
        for j in range(0, len(builds)):
            if builds[j]['confID'] == orders_ser[i]['fields']['configuration']:
                builds[j]['status'] = orders_ser[i]['fields']['status']

    context = {
        'title': 'Orders',
        'builds': builds,
    }
    return render(request, 'orders/view_orders.html', context)
