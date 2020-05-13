from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import resolve
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.apps import apps
from django.core.serializers import serialize
from . import models
from django.contrib.auth.decorators import login_required
from . import myFunctions as mf
from django.shortcuts import reverse

part_types = ['CPU','GPU','Motherboard','Ram_set', 'PSU',
 'Storage', 'Case', 'CPU_Cooler','Optical_Drive',
  'Sound_Card', 'Monitor', 'Operating_System']

def home(request):
    posts = models.Post.objects.all().order_by('-date_posted')

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'title': 'Home',
        'posts': posts,
    }
    return render(request, 'main/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'main/about.html', context)


def catalog(request, itemType='cpu'):
    if request.GET.get('itemID'):
        itemID = request.GET.get('itemID')
        return product(request, itemID, itemType)

    parts = apps.get_model('main', itemType).objects.all()
    parts = parts.order_by('Price')

    paginator = Paginator(parts, 20)
    page = request.GET.get('page')
    parts = paginator.get_page(page)

    context = {
        # 'ten': [1,2,3,4,5,6,7,8,9,10],
        # 'fifty': fifty = ['1'] * 50,
        'itemType': itemType,
        'parts': parts,
    }
    return render(request, 'main/catalog.html', context)

def product(request, itemID, itemType='cpu'):
    part = apps.get_model('main', itemType).objects.filter(id=itemID)
    part_serialized = serialize("python", part)[0]

    del part_serialized['fields']['Image']
    del part_serialized['fields']['Description']
    del part_serialized['fields']['Recommendations']
    context = {
        'part_serialized': part_serialized,
        'part': part.first(),
        'itemType': itemType,
        'itemID': itemID,
    }
    return render(request, 'main/product.html', context)

# @login_required
def configure(request):
    confID = request.GET.get('confID')
    selections = None
    if confID:
        conf = apps.get_model('main','Configuration').objects.filter(id = confID)
        if conf.first():
            selections = []
            conf_ser = serialize("python", conf)
            del conf_ser[0]['fields']['Date_Saved']
            sum = 0
            for key, value in conf_ser[0]['fields'].items():
                if value:
                    part = apps.get_model('main', key).objects.filter(id=value).first()
                    selections.append(part.__class__.__name__ + "-" + str(part.id))

    main_models = apps.get_models('main')
    all_parts = dict()
    for model in main_models:
        if model.__name__ in part_types:
            all_parts.update({model.__name__: model.objects.all()})
    
    temp = dict()
    for key, parts in all_parts.items():
        parts = parts.order_by('Price')
        paginator = Paginator(parts, 20)
        page = request.GET.get(f'page{key}')
        parts = paginator.get_page(page)
        temp.update({ key: parts })
    all_parts = temp

    context = {
        'all_parts': all_parts,
        'total': 0,
        'selections': selections,
        'message_text': None,
    }
    if request.method == 'POST':
        logic = mf.configure_logic(request)
        if logic[0]:
            context['selections'] = logic[0][0]
            context['message_text'] = logic[0][1]
            return render(request, 'main/configure.html', context)
        else:
            if 'Save' in request.POST:
                return render(request, 'main/configure_complete.html')
            elif 'Order' in request.POST:
                return HttpResponseRedirect(reverse('shopping-cart', kwargs={'confID': logic[1]}))

    return render(request, 'main/configure.html', context)


@login_required
def saved_builds(request):

    builds, conf_ser = mf.get_saved_builds(request.user)

    context = {
        'title': "Saved Builds",
        'builds': builds
    }
    return render(request, 'main/saved_builds.html', context)

def recommended_builds(request):

    builds, conf_ser = mf.get_saved_builds(None)

    context = {
        'title': "Saved Builds",
        'builds': builds
    }
    return render(request, 'main/recommended_builds.html', context)




