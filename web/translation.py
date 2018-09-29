from modeltranslation.translator import translator, TranslationOptions
from .models import Blog, TestModel, BlogGallery, Sliders, TextPages, TextPagesIcons, ProductCategories, Products, Successkeys, WebSettings

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'short_descr','description',)

class TestModelTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

class BlogGalleryTrans(TranslationOptions):
    fields = ('gallery_title', 'short_descr',)

class SlidersTrans(TranslationOptions):
    fields = ('title', 'short_descr',)

class TextPagesTrans(TranslationOptions):
    fields = ('title', 'short_descr','body',)

class TextPagesIconsTrans(TranslationOptions):
    fields = ('title', 'short_descr',)

class ProductCategoriesTrans(TranslationOptions):
    fields = ('title', 'short_descr',)

class ProductsTrans(TranslationOptions):
    fields = ('title', 'short_descr','body',)

class SuccesskeysTrans(TranslationOptions):
    fields = ('title', )

class WebSettingsTrans(TranslationOptions):
    fields = ('website_name', 'small_description','address')


translator.register(WebSettings, WebSettingsTrans)
translator.register(Successkeys, SuccesskeysTrans)
translator.register(Products, ProductsTrans)
translator.register(ProductCategories, ProductCategoriesTrans)
translator.register(TextPagesIcons, TextPagesIconsTrans)
translator.register(TextPages, TextPagesTrans)
translator.register(Sliders, SlidersTrans)
translator.register(BlogGallery, BlogGalleryTrans)
translator.register(Blog, BlogTranslationOptions)
translator.register(TestModel, TestModelTranslationOptions)
