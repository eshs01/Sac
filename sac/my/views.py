from django.shortcuts import render
from django.http import HttpResponse
from models import product

# Create your views here.
def base(request):
    
    Product = product.objects.all()
    return render(request, "my/base.html",{
        'message': Product
    })

