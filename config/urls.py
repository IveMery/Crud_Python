from django.contrib import admin
from django.urls import path,include
from laboratorio.views import indexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name= 'index'),
    path('laboratorio/', include('laboratorio.urls')),
]
