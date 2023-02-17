from django.shortcuts import render

from .models import Product, Category, Brand

# Create your views here.


def index(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'store/index.html', context)


def all_electronics(request, category_id=None, brand_id=None):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
    }

    if category_id and (brand_id is None):
        products = Product.objects.filter(category_id=category_id)
        context['products'] = products
    elif (category_id is None) and brand_id:
        products = Product.objects.filter(brand_id=brand_id)
        context['products'] = products
    else:
        products = Product.objects.all()
        context['products'] = products

    return render(request, 'store/all-electronics.html', context)


def product_info(request, product_id):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    product = Product.objects.get(id=product_id)
    similar_products = Product.objects.filter(brand_id=product.brand.id).order_by('?')[:5]

    context = {
        'categories': categories,
        'brands': brands,
        'product': product,
        'similar_products': similar_products,
    }

    return render(request, 'store/product_info.html', context)


def about(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'store/about.html', context)


def delivery_info(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'store/delivery.html', context)


def guarantee(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'store/guarantee.html', context)


def trade_in(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'store/trade_in.html', context)


def regularcustomers(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'store/regularcustomers.html', context)


def contacts(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'categories': categories,
        'brands': brands,
    }

    return render(request, 'store/contacts.html', context)
