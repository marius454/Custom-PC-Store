from django.shortcuts import render
from .models import Order, Payment_Info
from django.apps import apps
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from .forms import CheckoutForm, PaymentForm

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
