from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=128, unique=True, verbose_name='نام دپارتمان')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    created_at = jmodels.jDateTimeField(null=True, blank=True, verbose_name='تاریخ ایجاد دپارتمان')

    def __str__(self):
        return f'{self.department_name}'
    
    class Meta:
        verbose_name = 'دپارتمان'
        verbose_name_plural = 'دپارتمان ها'


class Collabrations(models.Model):
    full_name = models.CharField(max_length=128, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='دپارتمان')
    resume_file = models.FileField(upload_to='collabration/' ,verbose_name='فایل رزومه', null=True, blank=True)
    explanation = models.TextField(verbose_name='توضیحات بیشتر', null=True, blank=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت همکاری')
    is_seen = models.BooleanField(default=False, verbose_name='دیده شده / نشده')

    def __str__(self):
        return f'{self.full_name} {self.department}'
    
    class Meta:
        verbose_name = 'همکاری'
        verbose_name_plural = 'همکاری ها'


class HumanRecourceNeed(models.Model):
    company_name = models.CharField(max_length=128, verbose_name='نام شرکت')
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    job_title = models.CharField(max_length=128, verbose_name='عنوان شغلی')
    explanation = models.TextField(verbose_name='توضیحات بیشتر', null=True, blank=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت درخواست')
    is_seen = models.BooleanField(default=False, verbose_name='دیده شده / نشده')

    def __str__(self):
        return f'{self.company_name}'
    
    class Meta:
        verbose_name = 'درخواست منابع انسانی'
        verbose_name_plural = 'درخواست های منابع انساانی'
