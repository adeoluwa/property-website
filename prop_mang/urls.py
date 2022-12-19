from django.urls import path

from prop_mang import views

app_name = 'prop_mang'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.home, name='about'),
    path('contact/', views.home, name='contact'),
    path('apartment/', views.home, name='apartment'),
    path('apartment_details', views.apartment_details, name='apartment_details'),
    path('single', views.single, name='single')
]