from django.contrib import admin
# Register your models here.
from django.utils.translation import ugettext_lazy as _

#from parler.admin import TranslatableAdmin
from .models import Blog, BlogGallery, Sliders, TextPages, TextPagesIcons, ProductCategories, Products, Successkeys, Partners, WebSettings, TestModel



from modeltranslation.admin import TranslationAdmin

class BlogAdmin(TranslationAdmin):
    pass

class TestModelAdmin(TranslationAdmin):
    pass

class SlidersAdmin(TranslationAdmin):
    pass

class BlogGalleryAdmin(TranslationAdmin):
    pass

class TextPagesAdmin(TranslationAdmin):
    pass

class TextPagesIconsAdmin(TranslationAdmin):
    pass

class ProductCategoriesAdmin(TranslationAdmin):
    pass

class ProductsAdmin(TranslationAdmin):
    pass

class SuccesskeysAdmin(TranslationAdmin):
    pass

class WebSettingsAdmin(TranslationAdmin):
    pass









#admin header

admin.site.site_header = 'Moller website CMS'






    
admin.site.register(TestModel, TestModelAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogGallery, BlogGalleryAdmin)
admin.site.register(Sliders, SlidersAdmin)
admin.site.register(TextPages, TextPagesAdmin)
admin.site.register(TextPagesIcons, TextPagesIconsAdmin)
admin.site.register(ProductCategories, ProductCategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Successkeys, SuccesskeysAdmin)
admin.site.register(Partners)
admin.site.register(WebSettings, WebSettingsAdmin)

#admin.site.unregister(Group)