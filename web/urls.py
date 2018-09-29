from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index' ),
    #path('', views.IndexView.as_view(), name='index'),
    ##path('news_and_events/', views.blog_list, name='news_and_events' ),
    # ex: /blog/5/
    #path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('news_and_events/<slug:slug>/',views.blog_detail),
    #path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),

    path('about/', views.about_page, name='about_page' ),
    path('services/', views.services_list, name='services_list' ),
    # ex: /services/5/
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),

    path('products/', views.products_list, name='products_list' ),
    path('products_categories/<slug:slug>/', views.products_categories, name='products_categories' ),
    # ex: /products/5/
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('contactus/', views.contactus, name='contactus'),
    path('test/', views.test_page, name='test_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
