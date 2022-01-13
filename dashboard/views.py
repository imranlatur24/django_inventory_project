from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ProductModel,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User

#add flash messages
from django.contrib import messages

 #user enter  http://127.0.0.1:8000/dashboard first ask for login by decorators
@login_required(login_url='login')
def index(request):
    orders=Order.objects.all()
    products=ProductModel.objects.all()
    products_count = products.count()
    orders_count=orders.count()
    workers_count = User.objects.all().count()
    if request.method=='POST':
            form=OrderForm(request.POST)
            if form.is_valid(): #instance update on screen of product 
                instance=form.save(commit=False)
                instance.staff=request.user
                instance.save()
                return redirect('dashboard-index')
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'products_count':products_count,
        'orders_count':orders_count,
        'workers_count':workers_count,
    }
    return render(request,'dashboard/index.html',context)

@login_required(login_url='login')
def staff(request):
    workers=User.objects.all()
    orders=Order.objects.all()
    products=ProductModel.objects.all()
    products_count = products.count()
    orders_count=orders.count()
    workers_count = workers.count()
    context={
        'workers':workers,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count,
    }
    return render(request,'dashboard/staff.html',context)

@login_required(login_url='login')
def order(request):
    orders=Order.objects.all()
    products=ProductModel.objects.all()
    workers=User.objects.all()
    products_count = products.count()
    orders_count=orders.count()
    workers_count = workers.count()
    context={
        'orders':orders,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count,
    }
    return render(request,'dashboard/order.html',context)

@login_required(login_url='login')
def staff_details(request,pk):
    worker=User.objects.get(id=pk)
    print('workder id',worker)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=worker)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form=ProductForm(instance=worker)
    context = {
        'worker':worker,
        'form':form,
    }
    return render(request,'dashboard/staff_details.html',context)

@login_required(login_url='login')
def product(request):
    items=ProductModel.objects.all() #using ORM 
    products_count=items.count()
    orders=Order.objects.all()
    workers=User.objects.all()
    orders_count=orders.count()
    workers_count = workers.count()
    # items = ProductModel.objects.raw('select *from dashboard_ProductModel')
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been updated')
            return redirect('product')
    else:
        form=ProductForm()
    context = {
        'items':items,
        'form':form,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count,
    }
    return render(request,'dashboard/product.html',context)

@login_required(login_url='login')
def product_delete(request,pk):
    item = ProductModel.objects.get(id=pk)
    print('delete id ',item)
    if request.method == 'POST':
        item.delete()
        return redirect('product')
    context = {
        'item': item
    }
    return render(request,'dashboard/product.html',{'item':item})

@login_required(login_url='login')
def product_update(request,pk):
    item=ProductModel.objects.get(id=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form=ProductForm(instance=item)
    context = {
        'items':item,
        'form':form,
    }
    return render(request,'dashboard/update_product.html',context)


