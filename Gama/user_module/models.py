from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


class User(AbstractUser):
    personal_id = models.PositiveIntegerField(auto_created=True, editable=False, verbose_name='شماره پرسنلی')
    role = models.CharField(max_length=128, verbose_name='نقش')
    phone_number = models.CharField(max_length=11, verbose_name='تلفن همراه')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    groups = models.ManyToManyField(
        Group,
        related_name='users_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='users_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )