from django.db.models import Q

from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template_name = "homepage/index.html"
    ice_cream_list = IceCream.objects.values(
    'id', 'title', 'description'
    ).filter(
    is_published=True, is_on_main=True
    ).order_by('title')[1:4]
    context = {
        "ice_cream_list": ice_cream_list,
    }
    return render(request, template_name, context)

# from django.shortcuts import render

# from ice_cream.models import Category, IceCream

# def index(request):
#     template_name = 'homepage/index.html'
#     categories = Category.objects.values(
#         'id', 'output_order', 'title'
#     ).order_by(
#         # Сортируем записи по значению поля output_order,
#         # а если значения output_order у каких-то записей равны -
#         # сортируем эти записи по названию в алфавитном порядке.
#         'output_order', 'title'
#     )
#     context = {
#         'categories': categories
#     }
#     return render(request, template_name, context)