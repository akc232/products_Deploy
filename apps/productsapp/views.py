from django.shortcuts import render, redirect

from .models import Product
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    context={
        'products': Product.objects.all()
    }
    return render(request, 'productsapp/index.html', context)

def new(request):

    return render(request, 'productsapp/add.html')

def create(request):
    process = Product.objects.create_product(request.POST)

    if process == True:
        print process, "<----"

    return redirect('products:index')

def show(request, id):
    print id
    context={
        'products': Product.objects.filter(id=id)
    }
    return render(request, 'productsapp/show.html', context)

def edit(request, id):
    context={
        'products': Product.objects.filter(id=id)
    }
    return render(request, 'productsapp/edit.html', context)

def update(request, id):
    process= Product.objects.edit_product(request.POST)

    return redirect('products:index')

def delete(request, id):
    delete = Product.objects.get(id=id)
    delete.delete()

    return redirect('products:index')


# def show_product(request, id):
#     product_id= Product.objects.get(id=id)
#
#     return redirect(revers('products:show', id=id))






# index: Display all products
# show: Display a particular product
# new: Display a form to create a new product
# edit: Display a form to update a product
# create: Process information to create a new product
# update: Process information from the edit form and update the particular product
# destroy: Remove a product
