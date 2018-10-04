from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index' ), # home page
    path('about/', views.about_page, name='about_page' ), # About page
    path('services/', views.services_list, name='services_list' ), # Our services page
    path('services/<int:service_id>/', views.service_detail, name='service_detail'), # Service Detail page
    path('products/', views.products_list, name='products_list' ), # Products list
    path('products_categories/<slug:slug>/', views.products_categories, name='products_categories' ), # Products list by Categories 
    path('products/<slug:slug>/', views.product_detail, name='product_detail'), # Product Details Page
    path('news_and_events/', views.blog_list, name='news_and_events' ), # News and Events List
    path('news_and_events/<slug:slug>/',views.blog_detail), # News and Events Detail page
    path('contactus/', views.contactus, name='contactus'), # contact us page
    path('newslettersignup/', views.newsletter_signup, name='newsletter_signup'), # Newsletter subscription
    path('newsletterunsubscribe/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'), # Newsletter Unsubscription
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
