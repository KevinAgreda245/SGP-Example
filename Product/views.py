from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'Product/product_list.html', {'products': products})

def product_detail(request,id):
    product = get_object_or_404(Product,id = id)
    return render(request,'Product/product_detail.html',{'product':product})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Producto creado exitosamente')
            return redirect('product_list')
        else: 
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({'class': "form-control is-invalid"})
        return render(request,'Product/product_form.html',{'form':form})
    else: 
        form = ProductForm()
    return render(request,'Product/product_form.html',{'form':form})    

def product_update(request,id):
    product = get_object_or_404(Product,id = id)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,'Producto modificado exitosamente')
            return redirect('product_list')
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({'class': "form-control is-invalid"})
        return render(request,'Product/product_form.html',{'form':form, 'object': product})
    else: 
        form = ProductForm(instance=product)
    return render(request,'Product/product_form.html',{'form':form, 'object': product})

def product_delete(request,id):
    product = Product.objects.get(id= id)
    product.delete()
    messages.success(request, 'Producto eliminado exitosamente')
    return redirect('product_list')
