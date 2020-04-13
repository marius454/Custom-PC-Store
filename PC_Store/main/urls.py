from django.urls import path
# from .views import PostListView
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('about/', views.about, name='store-about'),
    path(r'catalog/', views.catalog, name='store-catalog'),
    path(r'catalog/<itemType>/', views.catalog, name='store-catalog'),
    path(r'catalog/<itemType>/?itemID=<itemID>', views.catalog, name='store-catalog'),
    # path('catalog/cpu/', views.catalog, name = 'cpu-catalog'),
    # path('catalog/gpu/', views.catalog, name = 'gpu-catalog'),
    # path('catalog/motherboard/', views.catalog, name = 'motherboard-catalog'),
    # path('catalog/ram_set/', views.catalog, name = 'ram_set-catalog'),
    # path('catalog/psu/', views.catalog, name = 'psu-catalog'),
    # path('catalog/storage/', views.catalog, name = 'storage-catalog'),
    # path('catalog/case/', views.catalog, name = 'case-catalog'),
    # path('catalog/cpu_cooler/', views.catalog, name = 'cpu_cooler-catalog'),
]