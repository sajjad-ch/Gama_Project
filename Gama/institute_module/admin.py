from django.contrib import admin
import nested_admin.nested
from .models import *
import nested_admin
# Register your models here.


class RegisterationModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_seen', 'created_at')
    search_fields = ('full_name',)
    list_filter = ('is_seen', 'created_at',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.is_seen = True
        return super().save_model(request, obj, form, change)


admin.site.register(Registeration, RegisterationModelAdmin)
admin.site.register(Slider)
admin.site.register(HeadlineCourse)
admin.site.register(LessonsHeadline)
admin.site.register(CommentsAndSuggestions)
admin.site.register(InstitueData)

class LessonsHeadlineAdmin(nested_admin.nested.NestedStackedInline):
    model = LessonsHeadline
    # sortable_field_name = 'lesson_name'


class HeadlineCourseAdmin(nested_admin.nested.NestedStackedInline):
    model = HeadlineCourse
    # sortable_field_name = 'headline_name'
    inlines = [LessonsHeadlineAdmin]


class CourseAdmin(nested_admin.nested.NestedModelAdmin):
    inlines = [HeadlineCourseAdmin]

admin.site.register(Course, CourseAdmin)