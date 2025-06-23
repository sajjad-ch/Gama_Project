from django.contrib import admin
from .models import *
# Register your models here.


class CollabrationsModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_seen', 'created_at')
    search_fields = ('job_title',)
    list_filter = ('is_seen', 'created_at',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.is_seen = True
        return super().save_model(request, obj, form, change)
    

class HumanRecourceNeedModelAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'is_seen', 'created_at', 'job_title')
    search_fields = ('company_name',)
    list_filter = ('is_seen', 'created_at')
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.is_seen = True
        return super().save_model(request, obj, form, change)


admin.site.register(Department)
admin.site.register(Collabrations, CollabrationsModelAdmin)
admin.site.register(HumanRecourceNeed, HumanRecourceNeedModelAdmin)