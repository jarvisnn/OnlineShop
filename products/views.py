from django.shortcuts import render
from products.models import *
# Create your views here.

def index(request):

    list1 = {}
    for categoryLevel2 in CategoryLevel2.objects.all():
        list2 = {}
        for category in categoryLevel2.category_set.order_by('-id').all():
            if len(category.product_set.all()) > 0:
                list2[category] = category.product_set.order_by('-id').all()[:25]

        if len(list2) != 0:
            list1[categoryLevel2] = list2

    return render(request, 'products/index.html', {
        'category': CategoryLevel2.objects.all(), 'data': list1,
        'slideImages': SlideImage.objects.all(),
    })


def getProductWithCategory(request, category_id):

    categories = Category.objects.filter(id=int(category_id))

    if len(categories) == 0:
        return render(request, 'products/index.html', {
            'category': CategoryLevel2.objects.all(), 'data': {},
            'slideImages': SlideImage.objects.all(),
        })

    list1 = {}
    list2 = {}

    category = categories[0]
    categoryLevel2 = category.upperCategory

    if len(category.product_set.all()) > 0:
        list2[category] = category.product_set.order_by('-id').all()
    if len(list2) != 0:
        list1[categoryLevel2] = list2

    return render(request, 'products/index.html', {
        'category': CategoryLevel2.objects.all(), 'data': list1,
        'slideImages': SlideImage.objects.all(),
    })


def getProduct(request, product_id):
    products = Product.objects.filter(id=int(product_id))
    if len(products) == 0:
        return render(request, 'products/product.html', {
            'category': CategoryLevel2.objects.all(),
        })
    else:
        products[0].view += 1
        products[0].save()

        images = []
        if products[0].image1:
            images.append(products[0].image1)
        if products[0].image2:
            images.append(products[0].image2)
        if products[0].image3:
            images.append(products[0].image3)
        if products[0].image4:
            images.append(products[0].image4)
        if products[0].image5:
            images.append(products[0].image5)
        for img in products[0].image_set.all():
            images.append(img.image)

        return render(request, 'products/product.html', {
            'category': CategoryLevel2.objects.all(), 'product': products[0],
            'images': images,
        })


def search(request):
    keyword = ""
    if "keyword" in request.GET:
        keyword = request.GET["keyword"]

    products = []
    for item in Product.objects.all():
        cc = 0
        for word in keyword.split():
            cc += item.name.count(word) * 2 + item.description.count(word)
        products.append((cc, item))

    products.sort(key=lambda tup: -tup[0])

    sortedProducts = []
    for product in products:
        if (product[0] != 0):
            sortedProducts.append(product[1])

    return render(request, 'products/index.html', {
        'category': CategoryLevel2.objects.all(),
        'products': sortedProducts,
        'keyword': keyword,
        'slideImages': SlideImage.objects.all(),
    })


def makeOrders(request):
    return render(request, 'products/order.html')
