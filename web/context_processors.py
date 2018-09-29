
from .models import ProductCategories, WebSettings, Blog

def templateRequiredData(request):
    categories = ProductCategories.objects.order_by('pk')
    categories_footer = ProductCategories.objects.order_by('pk')[:6]
    webSettings = WebSettings.objects.get(pk=1)
    artFooter = Blog.objects.order_by('title')[:3]
    return {'categories': categories, 'webSettings': webSettings, 'artFooter': artFooter, 'categories_footer':categories_footer}



