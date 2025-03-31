from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=128, unique=True, verbose_name='نام دپارتمان')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')

    def __str__(self):
        return f'{self.department_name}'
    
    class Meta:
        verbose_name = 'دپارتمان'
        verbose_name_plural = 'دپارتمان ها'


class Collabrations(models.Model):
    first_name = models.CharField(max_length=128, verbose_name='نام')
    last_name = models.CharField(max_length=128, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='دپارتمان')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.department}'
    
    class Meta:
        verbose_name = 'همکاری'
        verbose_name_plural = 'همکاری ها'


class HumanRecourceNeed(models.Model):
    first_name = models.CharField(max_length=128, verbose_name='نام')
    last_name = models.CharField(max_length=128, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')
    job_title = models.CharField(max_length=128, verbose_name='عنوان شغلی')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='دپارتمان')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.department}'
    
    class Meta:
        verbose_name = 'همکاری'
        verbose_name_plural = 'همکاری ها'
