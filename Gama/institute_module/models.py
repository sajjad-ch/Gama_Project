from django.utils import timezone
from django.db import models
from staff_module.models import Department
from django_jalali.db import models as jmodels
# Create your models here.

course_age = (
    ('خردسال', 'خردسال'),
    ('نوجوان', 'نوجوان'),
    ('جوان', 'جوان'),
    ('بزرگسال', 'بزرگسال'),
    ('تمامی سنین', 'تمامی سنین'),
)
type_of_sliders = (
    ('خبر', 'خبر'),
    ('تخفیفات', 'تخفیفات'),
)

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
    course_start_date = jmodels.jDateTimeField(null=True, blank=True, verbose_name='زمان شروع دوره')
    rank = models.FloatField(verbose_name='امتیاز دوره', default=0.0)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
    is_registering = models.BooleanField(default=False, verbose_name='در حال ثبت نام')
    is_completing_registering = models.BooleanField(default=False, verbose_name='تکمیل ظرفیت')

    def __str__(self):
        return f'{self.course_name} در {self.course_department}'

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def time_until_start(self):
        now = timezone.now()
        return max(self.course_start_date - now, timezone.timedelta(0))


class HeadlineCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='دوره')
    headline_name = models.CharField(max_length=128, verbose_name='نام سرفصل')

    def __str__(self):
        return f'{self.headline_name} در {self.course.course_name}'
    
    class Meta:
        verbose_name = 'سر فصل'
        verbose_name_plural = 'سر فصل ها'
    

class LessonsHeadline(models.Model):
    headline = models.ForeignKey(HeadlineCourse, verbose_name='سر فصل', on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=128, verbose_name='نام درس')

    def __str__(self):
        return self.lesson_name
    
    class Meta:
        verbose_name = 'درس سرفصل'
        verbose_name_plural = 'درس های سر فصل'


class Registeration(models.Model):
    full_name = models.CharField(max_length=128, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='دوره')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت نام')
    is_seen = models.BooleanField(default=False, verbose_name='دیده شده / نشده')

    def __str__(self):
        return f'{self.full_name} {self.course}'

    class Meta:
        verbose_name = 'ثبت نامی'
        verbose_name_plural = 'ثبت نامی ها'


class CommentsAndSuggestions(models.Model):
    full_name = models.CharField(max_length=128, verbose_name='نام و نام خانوادگی')
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    comment_or_suggestion = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت نظر')

    def __str__(self):
        return f'{self.full_name} با شماره همراه {self.phone_number}'
    
    class Meta:
        verbose_name = 'نظر یا پیشنهاد'
        verbose_name_plural = 'نظرات و پیشنهادات' 


class Slider(models.Model):
    slider_name = models.CharField(max_length=128, verbose_name='نام اسلایدر')
    slider_type = models.CharField(max_length=128, verbose_name='نوع اسلایدر', choices=type_of_sliders)
    description = models.CharField(max_length=512, verbose_name='توضیحات اسلایدر')
    slider_picture = models.ImageField(upload_to='sliders/', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد اسلایدر')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return f'{self.slider_name} {self.slider_type}'
    

class InstitueData(models.Model):
    initial_data = models.CharField(default='اطلاعات موسسه', max_length=128)
    successful_student = models.PositiveIntegerField(default=0, verbose_name='فراگیران موفق')
    ongoing_courses = models.PositiveIntegerField(default=0, verbose_name='دوره های در حال برگزاری')
    your_approval = models.PositiveIntegerField(default=0, verbose_name='رضایت شما')
    experienced_teachers = models.PositiveIntegerField(default=0, verbose_name='اساتید مجرب ما')
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تا تاریخ')

    class Meta:
        verbose_name = 'اطلاعات موسسه'
        verbose_name_plural = 'اطلاعات های موسسه'

    def __str__(self):
        return f'{self.initial_data} تا تاریخ {self.created_at}'
    