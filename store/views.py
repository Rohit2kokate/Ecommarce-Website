from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def hello(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})