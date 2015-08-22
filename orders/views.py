from django.shortcuts import render
from products.models import Product, Category, CategoryLevel2
from django.http import *
from orders.models import *
# Create your views here.


def index(request):
    order = None

    if request.method == 'POST':
        order = Order(phoneNumber=request.POST['phone'],address=request.POST['address'],
            customer=request.POST['name'], products=request.POST['products'],
            note=request.POST['note'], status='processing', price=request.POST['cost'])

        if order.customer != '' and order.phoneNumber != '' and order.address != '' and order.note != '':
            order.save()
            return render(request, 'orders/order.html', {
                'thankyou': True,
            })

    if "items" in request.COOKIES:
        itemList = request.COOKIES["items"].split("-")
        productList = []

        for item in itemList:
            if item.isdigit():
                list = Product.objects.filter(id=int(item))
                if (len(list) > 0):
                    productList.append(list[0])
        return render(request, 'orders/order.html', {
            'products': productList, 'order': order,
        })
    else:
        return render(request, 'orders/order.html', { 'order': order, })
