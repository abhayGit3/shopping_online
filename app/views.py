from django import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.forms import Form
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import  CustomerRegistrationForm,CustomerProfileForm, FeedbackProfileForm
from django.contrib import messages
from app import models
from app.models import Customer, Feedback
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class ProductView(View):
  def get(self, request):
     totalitem=0
     kurta= Product.objects.filter(category='mk')
     boys= Product.objects.filter(category='kb')
     girls= Product.objects.filter(category='kg')
     saree=Product.objects.filter(category='wsa')
     mala=Product.objects.filter(category='ml')
     brooch=Product.objects.filter(category='br')
     if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
     return render(request, 'app/home.html',{'kurta':kurta,'boys':boys,'girls':girls,'totalitem':totalitem,'saree':saree,'mala':mala,'brooch':brooch})


class ProductDetailView(View):
    def get(self,request,pk):
       totalitem=0
       product= Product.objects.get(pk=pk)
       item_already_in_cart =False
       if request.user.is_authenticated:
        item_already_in_cart=Cart.objects.filter(Q(product=product.id)& Q(user=request.user)).exists()
        if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
       return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart,'totalitem':totalitem})


@login_required
def add_to_cart(request):
 totalitem=0
 user=request.user
 product_id=request.GET.get('prod_id')
 product=Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 if request.user.is_authenticated:
  totalitem= len(Cart.objects.filter(user=request.user))
 return redirect('/cart',{'totalitem':totalitem})


def show_cart(request):
 if request.user.is_authenticated:
     totalitem=0
     user=request.user
     cart=Cart.objects.filter(user=user)
     #print(cart)
     amount=0.0
     shipping_amount=70.0
     totalamount=0.0
     cart_product=[p for p in Cart.objects.all() if p.user==user]
     #print(cart_product)
     if request.user.is_authenticated:
      totalitem= len(Cart.objects.filter(user=request.user))
     if cart_product:
         for p in cart_product:
             tempamount=(p.quantity * p.product.discounted_price)
             amount+=tempamount
             totalamount=amount+shipping_amount
         return render(request, 'app/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount,'shipping_amount':shipping_amount,'totalitem':totalitem})
     else:
         return render(request,'app/emptycart.html')    

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 totalitem=0
 add =Customer.objects.filter(user=request.user)
 if request.user.is_authenticated:
  totalitem= len(Cart.objects.filter(user=request.user))
 return render(request, 'app/address.html',{'add':add,'active':'btn-warning','totalitem':totalitem})

def orders(request):
 totalitem=0
 op=OrderPlaced.objects.filter(user=request.user)
 if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
 return render(request, 'app/orders.html',{'order_placed':op,'totalitem':totalitem})



def kurta(request, data=None):
    totalitem=0
    if data == None:
        kurta = Product.objects.filter(category='mk')
    elif data=='Manyawar' or data=='Fabindia':
        kurta = Product.objects.filter(category='mk').filter(brand=data)
    elif data=='below':
        kurta=Product.objects.filter(category='mk').filter(discounted_price__lt=500)
    elif data=='above':
        kurta=Product.objects.filter(category='mk').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/kurta.html',{'kurta':kurta,'totalitem':totalitem})

def sherwani(request, data=None):
    totalitem=0
    if data == None:
        sherwani = Product.objects.filter(category='msh')
    elif data=='Manyawar' or data=='Fabindia':
        sherwani = Product.objects.filter(category='msh').filter(brand=data)
    elif data=='below':
        sherwani=Product.objects.filter(category='msh').filter(discounted_price__lt=1000)
    elif data=='above':
        sherwani=Product.objects.filter(category='msh').filter(discounted_price__gt=1000)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/sherwani.html',{'sherwani':sherwani,'totalitem':totalitem})

def suit(request, data=None):
    totalitem=0
    if data == None:
        suit = Product.objects.filter(category='ms')
    elif data=='Manyawar' or data=='Fabindia':
        suit = Product.objects.filter(category='ms').filter(brand=data)
    elif data=='Peter_England' or data=='Nykaa_Fashion':
        suit = Product.objects.filter(category='ms').filter(brand=data)
    elif data=='below':
        suit=Product.objects.filter(category='ms').filter(discounted_price__lt=1000)
    elif data=='above':
        suit=Product.objects.filter(category='ms').filter(discounted_price__gt=1000)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/suit.html',{'suit':suit,'totalitem':totalitem})

def kurti(request, data=None):
    totalitem=0
    if data == None:
        kurti = Product.objects.filter(category='wk')
    elif data=='Biba' or data=='Nykaa_Fashion':
        kurti = Product.objects.filter(category='wk').filter(brand=data)
    elif data=='below':
        kurti=Product.objects.filter(category='wk').filter(discounted_price__lt=500)
    elif data=='above':
        kurti=Product.objects.filter(category='wk').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/kurti.html',{'kurti':kurti,'totalitem':totalitem})

def saree(request, data=None):
    totalitem=0
    if data == None:
        saree = Product.objects.filter(category='wsa')
    elif data=='FabIndia' or data=='Kalaniketan':
        saree = Product.objects.filter(category='wsa').filter(brand=data)
    elif data=='below':
        saree=Product.objects.filter(category='wsa').filter(discounted_price__lt=2500)
    elif data=='above':
        saree=Product.objects.filter(category='wsa').filter(discounted_price__gt=2500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/saree.html',{'saree':saree,'totalitem':totalitem})

def women_suit(request, data=None):
    totalitem=0
    if data == None:
        women_suit = Product.objects.filter(category='wsu')
    elif data=='FabIndia' or data=='Biba' or data=='Nykaa_Fashion':
        women_suit = Product.objects.filter(category='wsu').filter(brand=data)
    elif data=='below':
        women_suit=Product.objects.filter(category='wsu').filter(discounted_price__lt=500)
    elif data=='above':
        women_suit=Product.objects.filter(category='wsu').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/women_suit.html',{'women_suit':women_suit,'totalitem':totalitem})

def boys(request, data=None):
    totalitem=0
    if data == None:
        boys = Product.objects.filter(category='kb')
    elif data=='FabIndia' or data=='Manyawar' or data=='Nykaa_Fashion' or data=='Peter_England':
        boys = Product.objects.filter(category='kb').filter(brand=data)
    elif data=='below':
        boys=Product.objects.filter(category='kb').filter(discounted_price__lt=500)
    elif data=='above':
        boys=Product.objects.filter(category='kb').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/boys.html',{'boys':boys,'totalitem':totalitem})

def girls(request, data=None):
    totalitem=0
    if data == None:
        girls = Product.objects.filter(category='kg')
    elif data=='FabIndia' or data=='Manyawar' or data=='Nykaa_Fashion' or data=='Biba':
        girls = Product.objects.filter(category='kg').filter(brand=data)
    elif data=='below':
        girls=Product.objects.filter(category='kg').filter(discounted_price__lt=500)
    elif data=='above':
        girls=Product.objects.filter(category='kg').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/girls.html',{'girls':girls,'totalitem':totalitem})

def brooch(request, data=None):
    totalitem=0
    if data == None:
        brooch = Product.objects.filter(category='br')
    elif data=='Manyawar' or data=='Nykaa_Fashion':
        brooch = Product.objects.filter(category='br').filter(brand=data)
    elif data=='below':
        brooch=Product.objects.filter(category='br').filter(discounted_price__lt=500)
    elif data=='above':
        brooch=Product.objects.filter(category='br').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/brooch.html',{'brooch':brooch,'totalitem':totalitem})

def mala(request, data=None):
    totalitem=0
    if data == None:
        mala = Product.objects.filter(category='ml')
    elif data=='Manyawar' or data=='Nykaa_Fashion':
        mala = Product.objects.filter(category='ml').filter(brand=data)
    elif data=='below':
        mala=Product.objects.filter(category='ml').filter(discounted_price__lt=500)
    elif data=='above':
        mala=Product.objects.filter(category='ml').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/mala.html',{'mala':mala,'totalitem':totalitem})

def safa(request, data=None):
    totalitem=0
    if data == None:
        safa = Product.objects.filter(category='sf')
    elif data=='Manyawar' or data=='Nykaa_Fashion':
        safa = Product.objects.filter(category='sf').filter(brand=data)
    elif data=='below':
        safa=Product.objects.filter(category='sf').filter(discounted_price__lt=500)
    elif data=='above':
        safa=Product.objects.filter(category='sf').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/safa.html',{'safa':safa,'totalitem':totalitem})

def juti(request, data=None):
    totalitem=0
    if data == None:
        juti = Product.objects.filter(category='jt')
    elif data=='Manyawar' or data=='Nykaa_Fashion':
        juti = Product.objects.filter(category='jt').filter(brand=data)
    elif data=='below':
        juti=Product.objects.filter(category='jt').filter(discounted_price__lt=1000)
    elif data=='above':
        juti=Product.objects.filter(category='jt').filter(discounted_price__gt=1000)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/juti.html',{'juti':juti,'totalitem':totalitem})

def jewellery(request, data=None):
    totalitem=0
    if data == None:
        jewellery = Product.objects.filter(category='jw')
    elif data=='Manyawar' or data=='Nykaa_Fashion':
        jewellery = Product.objects.filter(category='jw').filter(brand=data)
    elif data=='below':
        jewellery=Product.objects.filter(category='jw').filter(discounted_price__lt=5000)
    elif data=='above':
        jewellery=Product.objects.filter(category='jw').filter(discounted_price__gt=5000)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/jewellery.html',{'jewellery':jewellery,'totalitem':totalitem})

def kamarpatta(request, data=None):
    totalitem=0
    if data == None:
        kamarpatta = Product.objects.filter(category='kp')
    elif data=='Manyawar' or data=='Nykaa_Fashion':
        kamarpatta = Product.objects.filter(category='kp').filter(brand=data)
    elif data=='below':
        kamarpatta=Product.objects.filter(category='kp').filter(discounted_price__lt=500)
    elif data=='above':
        kamarpatta=Product.objects.filter(category='kp').filter(discounted_price__gt=500)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/kamarpatta.html',{'kamarpatta':kamarpatta,'totalitem':totalitem})

def earrings(request, data=None):
    totalitem=0
    if data == None:
        earrings = Product.objects.filter(category='er')
    elif data=='Manyawar' or data=='Nykaa_Fashion':
        earrings = Product.objects.filter(category='er').filter(brand=data)
    elif data=='below':
        earrings=Product.objects.filter(category='er').filter(discounted_price__lt=100)
    elif data=='above':
        earrings=Product.objects.filter(category='er').filter(discounted_price__gt=100)
    if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
    return render(request, 'app/earrings.html',{'earrings':earrings,'totalitem':totalitem})










class CustomerRegistrationView(View):
    
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations!! You are registered Successfully.')
       
        return render(request,'app/customerregistration.html',{'form':form}) 

class FeedbackView(View):
    def get(self,request):
        form=FeedbackProfileForm()
        return render(request,'app/feedback.html',{'form':form})
    def post(self,request):
        form=FeedbackProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations!! Feedback Submitted Successfully.')
       
        return render(request,'app/feedback.html',{'form':form}) 

@login_required
def checkout(request):
 totalitem=0
 user=request.user
 add=Customer.objects.filter(user=user)
 cart_items= Cart.objects.filter(user=user)
 amount=0.0
 shipping_amount=70.0
 totalamount=0.0
 cart_product = [p for p in Cart.objects.all() if p.user == request.user]
 if cart_product:
  for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
 totalamount=amount+shipping_amount
 if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
 return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cart_items':cart_items,'totalitem':totalitem})

def payment_done(request):
 
 user=request.user
 custid=request.GET.get('custid')
 customer=Customer.objects.get(id=custid)
 cart=Cart.objects.filter(user=user)
 for c in cart:
  OrderPlaced(user=user,customer=customer, product=c.product, quantity=c.quantity).save()
  c.delete()
 
 return redirect("orders")


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    totalitem=0
    def get(self,request):
        form = CustomerProfileForm()
        if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
        return render(request,'app/profile.html',{'form':form,'active':'btn-warning','totalitem':totalitem})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Profile Updated Successfully')
        if request.user.is_authenticated:
         totalitem= len(Cart.objects.filter(user=request.user))
        return render(request, 'app/profile.html', {'form':form,'active':'btn-warning','totalitem':totalitem})


def plus_cart(request):
    
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount':amount,
            'totalamount' : amount + shipping_amount
            }
        
        return JsonResponse(data)

def minus_cart(request):
    
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount':amount,
            'totalamount' : amount + shipping_amount
            }
        
        return JsonResponse(data)

def remove_cart(request):
    
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            totalamount = amount 

        data = {
            'amount':amount,
            'totalamount':amount + shipping_amount
            }
        
        return JsonResponse(data)

