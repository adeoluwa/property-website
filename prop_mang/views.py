from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def apartment(request):
    return render(request, 'apartments.html')

def apartment_details (request):
    return render(request, 'apartment-detail.html')

def single(request):
    return render(request, 'single.html')

