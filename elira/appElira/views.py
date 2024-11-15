from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'appElira/home.html')

def about_page(request):
    return render(request, 'appElira/about.html')

def coupons_page(request):
    return render(request, 'appElira/coupons.html')

def stores_page(request):
    return render(request, 'appElira/stores.html')

def connect_page(request):
    return render(request, 'appElira/connect.html')

def sign_page(request):
    return render(request, 'appElira/sign.html')