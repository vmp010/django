from django.contrib import admin

from .models import RecordE, CategoryE,RecordR,CategoryR


# Register your models here.
class RecordRAdmin(admin.ModelAdmin):
    list_filter=('categoryR',)
    search_fields=('categoryR','date')
    ordering=('date',)
class RecordEAdmin(admin.ModelAdmin):
    list_filter=('categoryE')
    search_fields=('categoryE','date')
    ordering=('date',)

admin.site.register(RecordE)
admin.site.register(CategoryE)
admin.site.register(RecordR,RecordRAdmin)
admin.site.register(CategoryR)
