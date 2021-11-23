import datetime
from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product, Order
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,

                                                        'cart_product_form': cart_product_form})


def report(request):
    if 'report' in request.POST:
        period = request.POST['report']
        startdate = datetime.date.today()
        enddate = startdate + timedelta(days=6)
        Order.objects.all.filter(date__range=[startdate, enddate])
    return render(request=request, template_name='shop/report.html')




