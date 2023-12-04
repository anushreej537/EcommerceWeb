from django.shortcuts import render
from .models import *
from django.views import View
# def home(request):
#  return render(request, 'app/home.html')

class Productdetail(View):
 def get(self,request):
  topwear = Product.objects.filter(category = 'TW')
  bottomwear = Product.objects.filter(category = 'BW')
  mobile = Product.objects.filter(category = 'M')
  laptop = Product.objects.filter(category = 'L')
  return render(request, 'app/home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile,'laptop':laptop})
  


def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
