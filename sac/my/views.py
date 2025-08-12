from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product
from django.http import Http404
from .forms import Pform

# Create your views here.
def base(request):
        
    Product = product.objects.all()
    if request.method == "POST":
        search_query = request.POST.get("Product","")
        if search_query:
            Product = Product.filter(
                name__icontains=search_query
            )
    return render(request, "my/base.html",{
        'message': Product
    })

def details(request, product_id):
    if product.objects.filter(id=product_id).exists():
        sproduct = product.objects.get(id=product_id)
    else:
        raise Http404("product not found ")
    if request.method == "POST":
        sproduct.delete()
        return redirect('base')

    return render(request, "my/details.html",{
        "message":sproduct
    })
def add(request):
    if request.method == 'POST':
        form = Pform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base')
        else:
            print("form is invalid, returning 400")
            context = {
                'form': form
            }
            return render(request, "my/add.html", context, status=400)
        #the above basically keep the info in and tell what wrong with ur given data 
    else:
        form = Pform()
        context = {
            'form': form
        }
        return render(request, "my/add.html", context)
    
