from django.shortcuts import render, HttpResponse
from home.models import Product
# Create your views here.
def home(request):
    products_for_home=Product.objects.all()
    return render(request,'home.html',{'products': products_for_home})

def sign_in_form(request):
    return render(request,'sign_in_form.html')

def login_form(request):
    return render(request,'login_form.html')

def login(request):
    return HttpResponse("Login successful")

def sign_in(request):
    return HttpResponse("Sign in successful")

def logout(request):
    return HttpResponse("Logged out successfully")

def inventory(request):
    return render(request,'inventory.html')