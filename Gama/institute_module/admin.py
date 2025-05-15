from django.contrib import admin
import nested_admin.nested
from .models import *
import nested_admin
# Register your models here.

admin.site.register(Registeration)
admin.site.register(Slider)
admin.site.register(HeadlineCourse)
admin.site.register(LessonsHeadline)
admin.site.register(CommentsAndSuggestions)

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