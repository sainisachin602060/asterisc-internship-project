from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Product

def home(request):
    data=Product.objects.all()

    return render(request,'home.html',{'data':data})


