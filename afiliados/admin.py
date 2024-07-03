from django.contrib import admin
from .models import Afiliado, Mesa

# Register your models here.
class AfiliadoAdmin(admin.ModelAdmin):
    list_display = (
        'apellidos',
        'nombres',
        'dni',
        'mesa',
    )

    search_fields = ('apellidos','dni',)

admin.site.register(Afiliado,AfiliadoAdmin)
admin.site.register(Mesa)
