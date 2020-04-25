from django.shortcuts import render
from django.http import HttpResponse
from django.urls import resolve
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.apps import apps
from django.core.serializers import serialize
from . import models
from django.contrib.auth.decorators import login_required


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
    }
    return render(request, 'main/configure.html', context)

def configure_complete(request):
    if request.method == 'POST':
        radio_list = list()
        for name in part_types:
            radio_list.append(request.POST.get(name))

        configuration = models.Configuration(UserID = request.user)
        for item in radio_list:
            values = item.split("-")
            exec("configuration." + values[0] + " = apps.get_model('main', values[0]).objects.filter(id=values[1]).first()")

        configuration.save()
        
    context={
        'title': "Configuration Complete"
    }
    return render(request, 'main/configure_complete.html')
    


    