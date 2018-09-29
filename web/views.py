from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404, render
from django.template import loader

from django.urls import reverse
from django.views import generic 
from django.utils import timezone
from random import sample



from .models import Blog, BlogGallery, Sliders, TextPages, TextPagesIcons, Products, ProductCategories, Successkeys, Partners, WebSettings, TestModel
#
#from django.shortcuts import render

# Create your views here.








def blog_detail(request, slug):
    try:
        art = Blog.objects.get(slug=slug)
        art_img_list = BlogGallery.objects.filter(blog=art.id)
    except Blog.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'blog_detail.html', {'art': art, 'art_img_list':art_img_list, 'ii':0})



def index(request):
    context = {}
    art = Blog.objects.order_by('title')[:5]
    sliders_list = Sliders.objects.order_by('order')
    about = TextPages.objects.get(pk=1)
    abouticons = TextPagesIcons.objects.filter(page_id=1)[:4]
    #categories = ProductCategories.objects.order_by('pk')
    products = Products.objects.order_by('title')
    productsText = TextPages.objects.get(pk=2)
    partners = Partners.objects.all()
    # get random success keys
    succ_keys = Successkeys.objects.order_by('?')[:4]
   
        
    return render(request, 'index.html', {'art': art, 'sliders_list':sliders_list, 'about':about, 'abouticons':abouticons, 'products':products, 'succ_keys':succ_keys, 'partners':partners, 'productsText': productsText}, context)

def blog_list(request):
   # context = {}
    latest_blog_list = Blog.objects.order_by('dat')
    
    blogText = TextPages.objects.get(pk=4)
   
    return render(request, 'blog_list.html', {'latest_blog_list': latest_blog_list, 'blogText': blogText})

    


def about_page(request):
    try:
        context = {}
        about = TextPages.objects.get(pk=1)
        abouticons = TextPagesIcons.objects.filter(page_id=1).order_by('?')[:4]
        succ_keys = Successkeys.objects.order_by('?')[:4]
    except(TextPages.DoesNotExist):
        raise Http404("About page does not exist")
    return render(request, 'about.html', { 'about':about, 'abouticons':abouticons, 'succ_keys':succ_keys}, context)   
    #return HttpResponse("<h1>this is the About page</h1>")


def products_list(request):
    context= {}
    products = Products.objects.order_by('title')
    partners = Partners.objects.all()
    productsText = TextPages.objects.get(pk=2)
    return render(request, 'products.html', {'products': products, 'partners': partners, 'productsText': productsText}, context)


def products_categories(request, slug):
    context= {}
    productCat = ProductCategories.objects.get(slug=slug)
    products = Products.objects.filter(category=productCat.pk)
    return render(request, 'products_categories.html', { 'productCat': productCat, 'products':products}, context)


 

def product_detail(request, slug):
    try:
        product = Products.objects.get(slug=slug)
        same_category_products = Products.objects.filter(category=product.category)
    except Products.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'product_detail.html', {'product': product, 'same_category_products': same_category_products})

def services_list(request):
    try:
        context = {}
        services = TextPages.objects.get(pk=3)
        abouticons = TextPagesIcons.objects.filter(page_id=1).order_by('?')[:4]
        succ_keys = Successkeys.objects.order_by('?')[:4]
    except(TextPages.DoesNotExist):
        raise Http404("Services page does not exist")
    return render(request, 'services.html', { 'services':services, 'abouticons':abouticons, 'succ_keys':succ_keys}, context)

def contactus(request):
    try:
        context = {}
        
    except(TextPages.DoesNotExist):
        raise Http404("contact us page does not exist")
    return render(request, 'contactus.html', { }, context)


def service_detail(request, service_id):
    return HttpResponse("<h1>this is the Service detail</h1> %s." % service_id)


def test_page(request):
    tests = TestModel.objects.order_by('?')
    return render(request, "test.html", {'tests':tests})
