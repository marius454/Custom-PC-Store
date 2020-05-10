from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('about/', views.about, name='store-about'),
    path(r'catalog/', views.catalog, name='store-catalog'),
    path(r'catalog/<itemType>/', views.catalog, name='store-catalog'),
    path(r'catalog/<itemType>/?itemID=<itemID>', views.catalog, name='store-catalog'),
    path('configure/', views.configure, name='configure'),
    path('profile/saved-builds/', views.saved_builds, name='saved-builds'),
]