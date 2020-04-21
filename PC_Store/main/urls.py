from django.urls import path
# from .views import PostListView
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('about/', views.about, name='store-about'),
    path(r'catalog/', views.catalog, name='store-catalog'),
    path(r'catalog/<itemType>/', views.catalog, name='store-catalog'),
    path(r'catalog/<itemType>/?itemID=<itemID>', views.catalog, name='store-catalog'),
    path('configure/', views.configure, name='configure'),
]