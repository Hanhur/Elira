from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('about/', views.about_page, name = 'about'),
    path('coupons/', views.coupons_page, name = 'coupons'),
    path('stores/', views.stores_page, name = 'stores'),
    path('connect/', views.connect_page, name = 'connect'),
]