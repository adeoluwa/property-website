from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'prop_mang/index.html')

def about(request):
    return render(request, 'prop_mang/about.html')

def contact(request):
    return render (request, 'prop_mang/contact.html')

def apartment(request):
    return render(request, 'prop_mang/apartments.html')

def apartment_details (request):
    return render(request, 'apartment-detail.html')

def single(request):
    return render(request, 'single.html')

def news(request):
    return render(request, 'prop_mang/news.html')

