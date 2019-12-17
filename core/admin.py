from django.contrib import admin
from .models import Cliente, Tecnico, Ordentrabajo

# Register your models here.

class OrdentrabajoAdmin(admin.ModelAdmin):
    list_display = ['ot','cliente','fecha','tecnico']
    search_fields = ['ot']
    list_filter = ['cliente']
    list_per_page = 10

admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Ordentrabajo,OrdentrabajoAdmin)
