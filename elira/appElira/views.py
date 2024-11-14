from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'appElira/index.html')

def about_page(request):
    return render(request, 'appElira/about.html')