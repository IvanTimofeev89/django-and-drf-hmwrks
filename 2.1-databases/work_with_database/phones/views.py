from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sort')
    if sort_by:
        sort_dict = {
            'name': 'name',
            'min_price': 'price',
            'max_price': '-price',
        }
        phones = Phone.objects.all().order_by(sort_dict[sort_by])
        context = {
            'phones': phones
        }
        return render(request, template, context)

    else:
        phones = Phone.objects.all()
        context = {
            'phones': phones
        }
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
