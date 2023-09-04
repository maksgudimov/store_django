
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products.views import index,products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    #path('products/',products,name='products'),
    path('products/',include('products.urls',namespace='products')),
    path('users/',include('users.urls',namespace='users')),

]
# для отображения картинок по ссылке через админку
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

