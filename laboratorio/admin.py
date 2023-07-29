from django.contrib import admin
from .models import Laboratorio, DirectorGeneral ,Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio')    

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','laboratorio','f_fabricacion','p_costo','p_venta')    

admin.site.register(Laboratorio,LaboratorioAdmin)
admin.site.register(DirectorGeneral,DirectorAdmin)
admin.site.register(Producto,ProductoAdmin)