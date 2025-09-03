from django.shortcuts import render, HttpResponse, redirect
from home.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
# Create your views here.
def home(request):
    products_for_home=Product.objects.all()
    return render(request,'home.html',{'products': products_for_home})

def sign_in_form(request):
    
    return render(request,'sign_in_form.html')

def login_form(request):
    return render(request,'login_form.html')

def login_view(request):
    if request.method=='POST':
       email_from_user=request.POST.get('email')
       passworde=request.POST.get('password')
       user=authenticate(email=email_from_user, password=passworde)
       if user is not None:
          login(request, user)
          messages.success(request,"Logged in successfully!")
          return redirect('home')
       else:
          messages.error(request,"Invalid credentials, please try again!")
          return redirect('login_form')
    

def sign_in(request):
    # return HttpResponse("Sign in successful")
    if request.method=="POST":
     first_name=request.POST.get('first_name')
     last_name=request.POST.get('last_name')
     user_name=request.POST.get('user_name')
     phone_number=request.POST.get('phone_number')
     email=request.POST.get('email')
     password=request.POST.get('password')
     confirm_password=request.POST.get('confirm_password')
     profile_pic=request.FILES.get('profile_pic')
     if password != confirm_password:
        messages.error(request,"Passwords do not mathch!")
        return render(request,'sign_in_form.html')
     if User.objects.filter(username=user_name).exists():
       messages.error(request,"Username already taken!")
       return render(request,'sign_in_form.html')
     if User.objects.filter(email=email).exists():
       messages.error(request,"Email already registered!")
       return render(request,'sign_in_form.html')
     user=User.objects.create_user(username=user_name, email=email, password=password, first_name=first_name, last_name=last_name)
     user.save()
     profile=Profile(user=user, phone_number=phone_number, profile_image=profile_pic)
     profile.save()
     login(request, user)
     messages.success(request,"Account created successfully!")
     return redirect('home')

def logout_view(request):
    logout(request)
    messages.success(request,"Logged out successfully!")
    return redirect('/')

@login_required
def inventory(request):
    inventory_products=Product.objects.filter(product_seller_id=request.user)
    return render(request,'inventory.html',{'products': inventory_products})

def add_new_product_form(request):
   return render(request,'new_product.html')