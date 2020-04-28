from django.shortcuts import render
from django.http import HttpResponse
from django.urls import resolve
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.apps import apps
from django.core.serializers import serialize
from . import models
from django.contrib.auth.decorators import login_required
from . import myFunctions as mf


part_types = ['CPU','GPU','Motherboard','Ram_set', 'PSU', 'Storage', 'Case', 'CPU_Cooler']

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
  
# class PostListView(ListView):
#     model = models.Post
#     template_name = 'main/home.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']


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

    paginator = Paginator(parts, 2)
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

@login_required
def configure(request):
    
    main_models = apps.get_models('main')
    all_parts = {}
    for model in main_models:
        if model.__name__ in part_types:
            all_parts.update({model.__name__: model.objects.all()})
            
    context = {
        'all_parts': all_parts,
        'total': 0,
        'selections': None,
        'message_text': None,
    }
    if request.method == 'POST':
        logic = mf.configure_logic(request)
        if logic:
            context['selections'] = logic[0]
            print(context['selections'])
            context['message_text'] = logic[1]
            return render(request, 'main/configure.html', context)
        else:
            return render(request, 'main/configure_complete.html')

    return render(request, 'main/configure.html', context)



@login_required
def saved_builds(request):

    configurations = apps.get_model('main','Configuration').objects.filter(UserID=request.user)
    conf_ser = serialize("python", configurations)
    builds = list()
    for i in range(0,len(conf_ser)):
        del conf_ser[i]['fields']['UserID']
        del conf_ser[i]['fields']['Date_Saved']
        temp = list()
        sum = 0
        for key, value in conf_ser[i]['fields'].items():
            part = apps.get_model('main', key).objects.filter(id=value).first()
            temp.append(part)
            sum = sum + part.Price
        # temp = [sum] + temp
        temp.append(sum)
        builds.append(temp)

    context = {
        'title': "Saved Builds",
        'builds': builds
    }
    return render(request, 'main/saved_builds.html', context)