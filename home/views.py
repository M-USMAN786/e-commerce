from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def sign_in_form(request):
    return render(request,'sign_in_form.html')

def login_form(request):
    return render(request,'login_form.html')