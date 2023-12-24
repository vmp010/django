from django.contrib import admin

from .models import Record_E1, CategoryE,Record_R1,CategoryR,login_1


# Register your models here.
class RecordRAdmin(admin.ModelAdmin):
    list_display=('id','description')
    list_filter=('categoryR',)
    search_fields=('categoryR','date')
    ordering=('date',)

class RecordEAdmin(admin.ModelAdmin):
    list_display=('id','description')
    list_filter=('categoryE',)
    search_fields=('categoryE','date')
    ordering=('date',)

class loginAdmin(admin.ModelAdmin):
    list_display=('cName',)
    search_fields=('cName',)
    ordering=('id',)




admin.site.register(Record_E1,RecordEAdmin)
admin.site.register(CategoryE)
admin.site.register(Record_R1,RecordRAdmin)
admin.site.register(CategoryR)
admin.site.register(login_1,loginAdmin)

