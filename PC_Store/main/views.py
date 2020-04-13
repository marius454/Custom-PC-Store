from django.shortcuts import render
from django.http import HttpResponse
from django.urls import resolve
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.apps import apps
from django.core.serializers import serialize
from . import models

def home(request):
    posts = models.Post.objects.all().order_by('-date_posted')

    paginator = Paginator(posts, 1)
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
    # url = resolve(request.path_info).route
    # url = url.rsplit('/')[-2]
    if request.GET.get('itemID'):
        itemID = request.GET.get('itemID')
        return product(request, itemID, itemType)

    parts = apps.get_model('main', itemType).objects.all()
    # parts = get_parts(itemType)
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

    # part_fields = apps.get_model('main', itemType)._meta.get_fields()
    context = {
        # 'part_fields': part_fields,
        'part_serialized': part_serialized,
        'part': part.first(),
        'itemType': itemType,
        'itemID': itemID,
    }
    return render(request, 'main/product.html', context)
    

# def get_parts(name):
#     return apps.get_model('main', name).objects.all()
    # if name == 'cpu':
    #     return models.CPU.objects.all()
    # elif name == 'gpu':
    #     return models.GPU.objects.all()
    # elif name == 'motherboard':
    #     return models.Motherboard.objects.all()
    # elif name == 'ram_set':
    #     return models.Ram_set.objects.all()
    # elif name == 'psu':
    #     return models.PSU.objects.all()
    # elif name == 'storage':
    #     return models.Storage.objects.all()
    # elif name == 'case':
    #     return models.Case.objects.all()
    # else:
    #     return models.CPU_Cooler.objects.all()

