from django.shortcuts import render
from products.models import Product, Category, CategoryLevel2
from django.http import *
from orders.models import *
# Create your views here.


def index(request):

    if request.method == 'POST':
        order = Order(phoneNumber=request.POST['phone'],address=request.POST['address'],
            customer=request.POST['name'], products=request.POST['products'],
            note=request.POST['note'], status='processing', price=request.POST['cost'])
        order.save()
        return render(request, 'orders/order.html', {
            'thankyou': True,
        })

    if "items" in request.COOKIES:
        itemList = request.COOKIES["items"].split("-")
        productList = []

        for item in itemList:
            if item.isdigit():
                productList.append(Product.objects.filter(id=int(item))[0])
        return render(request, 'orders/order.html', {
            'products': productList,
        })
    else:
        return render(request, 'orders/order.html')
