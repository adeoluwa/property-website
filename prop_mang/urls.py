from django.urls import path

from prop_mang import views

app_name = 'prop_mang'

urlpatterns = [
  
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('apartment/', views.apartment, name='apartment'),
    path('apartment_details', views.apartment_details, name='apartment_details'),
    path('single', views.single, name='single'),
    path('news', views.news, name='news')
]