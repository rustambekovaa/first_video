from django.shortcuts import render,redirect


from .models import *

from django.http import HttpResponse,HttpResponseNotFound,Http404


menu = [{'title':"About site",'url_name':'about'},
        {'title':"Add article",'url_name':'addpage'},
        {'title':"Feedback",'url_name':'contact'},
        {'title':"Log_in",'url_name':'login'},
    ]


def index(request): 
    posts = Women.objects.all()
    context  = {
        'posts':posts,
        'menu':menu,
        'title':'Home page',
        'cat_selected':0
    }
    return render(request,'app1/index.html',context=context)


def about(request):
    return render(request,'app1/about.html', {'menu': menu,'title':'About us '})

def addpage(request):
    return HttpResponse(f"<h1> Add page </h1>")
 

def contact(request):
    return HttpResponse(f"<h1> Back contact</h1> <p>Call for number +996 557-707-885</p>")


def login(request):
    return HttpResponse(f"<h1> Login in </h1>")


def pageNoteFound(request,exeptio):
    return HttpResponseNotFound("<h1> Страница не найдена </h1>")


def show_post(request,post_id):
    return HttpResponse(f" Show id with id id = {post_id}")


def show_category(request,cat_id):
    posts = Women.objects.filter(cat_id = cat_id)

    if len(posts) == 0:
        raise Http404()

    context  = {
        'posts':posts,
        'menu':menu,
        'title':'Images about rubtik',
        'cat_selected':cat_id
    }
    return render(request,'app1/index.html',context=context)

