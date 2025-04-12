from django.db import models
from staff_module.models import Department
# Create your models here.

course_age = ()
type_of_sliders = ()

class Course(models.Model):
    course_picture = models.ImageField(upload_to='Courses/', verbose_name='تصویر دوره')
    course_name = models.CharField(max_length=128, verbose_name='نام دوره')
    course_time_hour = models.PositiveIntegerField(verbose_name='مدت زمان دوره')
    about_course = models.TextField(verbose_name='درباره دوره')
    course_price = models.PositiveIntegerField(verbose_name='قیمت دوره')
    course_department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='دپارتمان')
    course_level = models.CharField(max_length=128, null=True, blank=True, verbose_name='سطح')
    course_age = models.CharField(max_length=128, verbose_name='سن دوره', choices=course_age)
    course_session_number = models.PositiveSmallIntegerField(verbose_name='تعداد جلسات')
    rank = models.FloatField(verbose_name='امتیاز دوره', default=0.0)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
    is_registering = models.BooleanField(default=False, verbose_name='در حال ثبت نام')
    is_completing_registering = models.BooleanField(default=False, verbose_name='تکمیل ظرفیت')

    def __str__(self):
        return f'{self.course_name} در {self.course_department}'

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'


class Registeration(models.Model):
    first_name = models.CharField(max_length=128, verbose_name='نام')
    last_name = models.CharField(max_length=128, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='دوره')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.course}'

    class Meta:
        verbose_name = 'ثبت نامی'
        verbose_name_plural = 'ثبت نامی ها'


class CommentsAndSuggestions(models.Model):
    first_name_and_last_name = models.CharField(max_length=128, verbose_name='نام و نام خانوادگی')
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    comment_or_suggestion = models.TextField()

    def __str__(self):
        return f'{self.first_name_and_last_name} با شماره همراه {self.phone_number}'
    
    class Meta:
        verbose_name = 'نظر یا پیشنهاد'
        verbose_name_plural = 'نظرات و پیشنهادات' 


class Slider(models.Model):
    slider_name = models.CharField(max_length=128, verbose_name='نام اسلایدر')
    slider_type = models.CharField(max_length=128, verbose_name='نوع اسلایدر', choices=type_of_sliders)
    description = models.CharField(max_length=512, verbose_name='توضیحات اسلایدر')
    slider_picture = models.ImageField(upload_to='sliders/', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return f'{self.slider_name} {self.slider_type}'