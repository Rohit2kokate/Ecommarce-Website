from django.shortcuts import render,redirect
#from django.http import HttpResponse
from .models import Product,Category
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from.froms import SignUpForm
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Product

def category(request, foo):
    # Replace hyphens with spaces and strip whitespace
    category_name = foo.replace('-', ' ').strip()
    
    try:
        # Get the category (case-insensitive lookup would be better if needed)
        product_category = Category.objects.get(name__iexact=category_name)
        products = Product.objects.filter(product_category=product_category)
        
        return render(request, 'category.html', {
            'products': products,
            'product_category': product_category  # Pass the category to the template
        })
        
    except Category.DoesNotExist:
        messages.error(request, f"Category '{category_name}' doesn't exist")
        return redirect('hello')
        
    except Exception as e:
        # Log unexpected errors (you'll need to import logging)
        # logging.error(f"Error in category view: {str(e)}")
        messages.error(request, "An error occurred while processing your request")
        return redirect('hello')

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def hello(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You Have been login succesfully ..!")
            return redirect('hello')
        else:
            messages.error(request,("Unable to login Into Page..!"))    
            return redirect('login')
    else:
        return render(request,'login.html',{})

def logout_user(request):
   logout(request)
   messages.success(request,("YOU HAVE BEEN LOGOUT ..!"))
   return redirect('hello')

def register_user(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,("YOU HAVE BEEN REGISTERED ..!"))
            return redirect('hello')
        else:
            messages.error(request,("Unable to register Into Page..!"))
            return redirect('register')
        
    else:
        return render(request,'register.html',{'form':form})