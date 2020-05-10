from django.shortcuts import render
# from .models import Cart
from .models import Order
from django.apps import apps
from django.core.serializers import serialize
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

Total = 0

def CartView(request, confID):
    # cart = Cart.objects.all().first()
    # configuration = [cart.configuration]
    
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
    Total = sum
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
    conf = apps.get_model('main','Configuration').objects.filter(id = confID).first()
    new_order, created = Order.objects.get_or_create(configuration=conf.first())
        if created:
            new_order.userID = request.user
            new_order.total = Total
            new_order.save()


    context={

    }
    return render(request, "orders/checkout.html", context)

