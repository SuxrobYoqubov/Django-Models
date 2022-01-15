from dataclasses import field, fields
from django.contrib import admin
from .models import Talaba
# Register your models here.
class TalabaAdmin(admin.ModelAdmin):
    list_display = ['fio', 'phone', 'jinsi']
    fields=('fio', 'phone', 'jinsi', 'birth','image', 'file', 'show_image')
    readonly_fields = ('show_image',)
admin.site.register(Talaba, TalabaAdmin)
