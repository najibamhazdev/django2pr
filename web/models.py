from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import  RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Blog(models.Model):

    title = models.CharField(_("Title"), max_length = 200)
    short_descr = RichTextField(_("Brief"), max_length = 300, null=True, blank=True)
    dat = models.DateTimeField(_("Date"), null=True, blank=True)
    description = RichTextUploadingField(_("Description"), null=True, blank=True)
    author = models.CharField(_("Author"), max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=128)
    pic_thumb = models.ImageField(_("Photo"), upload_to='blog')


    def __str__(self):
        return self.title


class BlogGallery(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    gallery_title = models.CharField(_("Title"), max_length = 200, null=True, blank=True)
    short_descr = RichTextField(_("Brief"), max_length = 300, null=True, blank=True)
    picture = models.ImageField(_("Photo"), upload_to='blog_gallery')

    def __str__(self):
        return self.gallery_title


#------------------- Sliders -----------------------------

class Sliders(models.Model):
    title = models.CharField(_("Title"), max_length = 200)
    short_descr = RichTextField(_("Brief"), null=True, blank=True)
    link = models.CharField(_("Go To link"), max_length = 200, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(_("Photo"), upload_to='sliders', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title



class TextPages(models.Model):
    title = models.CharField(_("Page Title"), max_length = 200)
    short_descr = RichTextField(_("Brief"), null=True, blank=True)
    body= RichTextUploadingField(_("Description"), null=True, blank=True)
    slug = models.SlugField(max_length = 200)
    home_image = models.ImageField(_("Photo HomePage"), upload_to='text_pages', height_field=None, width_field=None, max_length=None, default='', null=True, blank=True)
    image = models.ImageField(_("Photo in Page"), upload_to='text_pages', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    header_image = models.ImageField(_("Photo Header"), upload_to='text_pages', height_field=None, width_field=None, max_length=None, default='', null=True, blank=True )
    backgroung_image_1 = models.ImageField(_("Photo Background 1"), upload_to='text_pages', height_field=None, width_field=None, max_length=None, default='', null=True, blank=True)
    background_image_2 = models.ImageField(_("Photo Background 2"), upload_to='text_pages', height_field=None, width_field=None, max_length=None, default='', null=True, blank=True )

    def __str__(self):
        return self.title

class TextPagesIcons(models.Model):
    page_id = models.ForeignKey(TextPages, on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length = 200, null=True, blank=True)
    short_descr = RichTextField(_("Brief"), null=True, blank=True)
    icon = models.CharField(max_length = 500, null=True, blank=True)

    def __str__(self):
        return self.title


class ProductCategories(models.Model):
    title = models.CharField(_("Title"), max_length = 200, null=True, blank=True)
    short_descr = RichTextField(_("Brief"), null=True, blank=True)
    icon = models.CharField(max_length = 500, null=True, blank=True)
    slug = models.SlugField(max_length = 200)
    image = models.ImageField(_("Photo"), upload_to='products_cat', height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    title = models.CharField(_("Item name"), max_length = 200, null=True, blank=True)
    short_descr = RichTextField(_("Brief"), null=True, blank=True)
    body = RichTextUploadingField(_("Description"), null=True, blank=True)
    slug = models.SlugField(max_length = 200)
    image = models.ImageField(_("Photo"), upload_to='products_cat', height_field=None, width_field=None, max_length=None, null=True, blank=True)


    def __str__(self):
        return self.title


class Successkeys(models.Model):
    title = models.CharField(_("Title"), max_length = 200, null=True, blank=True)
    icon = models.CharField(max_length = 200, null=True, blank=True)
    counter = models.IntegerField(_("Number"), null=True, blank=True)



    def __str__(self):
        return self.title


class Partners(models.Model):
    title = models.CharField(_("Partner name"),max_length = 200, null=True, blank=True)
    link = models.CharField(_("website link"),max_length = 200, null=True, blank=True)
    image = models.ImageField(_("Logo"), upload_to='partners', height_field=None, width_field=None, max_length=None, null=True, blank=True)


    def __str__(self):
        return self.title

class WebSettings(models.Model):
    website_name = models.CharField(_("Website name"), max_length=100, null=True, blank=True )
    small_description =  RichTextField(_("Brief"),null=True, blank=True)
    logo = models.ImageField(upload_to='settings', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    fav_icon = models.ImageField(upload_to='settings', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    phone_number_1 = models.CharField(_("Phone 1"),max_length=20,null=True, blank=True)
    phone_number_2 = models.CharField(_("Phone 2"),max_length=20, null=True, blank=True)
    phone_number_3 = models.CharField(_("phone 3"),max_length=20, null=True, blank=True)
    fax = models.CharField(_("FAX"),max_length=20, null=True, blank=True)
    email_1 = models.EmailField(_("Email 1"),max_length=254)
    email_2 = models.EmailField(_("Email 2"),max_length=254, null=True, blank=True)
    address = models.TextField(_("Address 1"), null=True, blank=True )
    address_2 = models.TextField(_("Address 2"), null=True, blank=True )
    facebook = models.CharField(_("Facebook link"), max_length=100, null=True, blank=True )
    twitter = models.CharField(_("Twitter link"), max_length=100, null=True, blank=True )
    instagram = models.CharField(_("Instagram link"), max_length=100, null=True, blank=True )
    linkedin= models.CharField(_("LinkedIn link"), max_length=100, null=True, blank=True )
    youtube_channel = models.CharField(_("Youtube link"), max_length=100, null=True, blank=True )

    def __str__(self):
        return self.website_name

class TestModel(models.Model):
    title=models.CharField(_("Title"), max_length=50)
    text = models.TextField(_("Description"))
    def __str__(self):
            return self.title

class NewsletterUser(models.Model):
    email = models.EmailField(_("Email"),max_length=254) 
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email           
