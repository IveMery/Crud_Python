from django.contrib import admin
from django.urls import path,include
from laboratorio.views import indexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name= 'index'),
    path('laboratorio/', include('laboratorio.urls')),
]
