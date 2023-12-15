from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.db.models import Q
from django.http import JsonResponse
# def home(request):
#  return render(request, 'app/home.html')

class Productdetail(View):
 def get(self,request):
  topwear = Product.objects.filter(category = 'TW')
  bottomwear = Product.objects.filter(category = 'BW')
  mobile = Product.objects.filter(category = 'M')
  laptop = Product.objects.filter(category = 'L')
  return render(request, 'app/home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile,'laptop':laptop})
  

class ProductDetailView(View):
 def get(self,request,pk):
  product = Product.objects.get(pk=pk)
  item_already_card = False
  if request.user.is_authenticated:
   item_already_card = Cart.objects.filter(Q(product=product.id)& Q(user=request.user)).exists()
   return render(request,'app/productdetail.html',{'item_already_card':item_already_card,'product':product})
  else:
    return render(request,'app/productdetail.html',{'item_already_card':item_already_card,'product':product})


def add_to_cart(request):
 user = request.user
 product_id = request.GET.get("prod_id")
 product = Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 return redirect('/cart')

def show_cart(request):
 if request.user.is_authenticated:
  user = request.user
  cart = Cart.objects.filter(user=user)
  ammount = 0.0
  shipping_ammount = 70.0
  total_ammount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user==user]
  if cart_product:
   for p in cart_product:
    temp_ammount = p.quantity*p.product.discounted_price
    ammount+= temp_ammount
    total_ammount =  ammount + shipping_ammount
    return render(request,'app/addtocart.html',{'carts':cart,
                                           'total_ammount':total_ammount,'ammount':ammount})
  else:
   return render(request,'app/emptycart.html')
   
def pluscart(request):
 if request.method == 'GET':
  prod_id = request.GET["prod_id"]
  c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity+=1
  c.save()
  ammount = 0.0
  shipping_ammount = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
   temp_ammount = p.quantity * p.product.discounted_price
   ammount += temp_ammount
   data = {'quantity':c.quantity,'ammount':ammount,'total_ammount':ammount + shipping_ammount}
   return JsonResponse(data)

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
