from django import template
from app1.models import *

register = template.Library()

@register.simple_tag(name = "getcats")
def get_categories(filter = None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)
    


@register.inclusion_tag('app1/list_catergories.html')
def show_categories(sort = None, cat_selected = 0):
    if not sort:
        cats =  Category.objects.all()
    else:
        cats =  Category.objects.order_by(sort)
          
    return{'cats':cats}