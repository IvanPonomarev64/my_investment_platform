from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    INVESTOR = 'IN'
    BORROWER = 'BR'
    ROLE_CHOICES = [
        (INVESTOR, 'Инвестор'),
        (BORROWER, 'Заемщик')
    ]
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    role = models.CharField(choices=ROLE_CHOICES, max_length=2, verbose_name='Роль')


class Passport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='passport')
    number = models.CharField(max_length=6)
    series = models.CharField(max_length=4)
    issued = models.TextField()
    date_of_issued = models.DateField()
    department_code = models.CharField(max_length=7)
    date_of_birth = models.DateField(null=True, blank=True,)
    place_of_birth = models.CharField(max_length=450)
    registration_address = models.CharField(max_length=450)


class PersonalAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    personal_account = models.IntegerField(default=0, verbose_name='Баланс')


class Company(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    inn = models.CharField(max_length=50, verbose_name='ИНН')
    kpp = models.CharField(max_length=50, verbose_name='КПП')
    ogrn = models.CharField(max_length=50, verbose_name='ОГРН')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    type = models.CharField(max_length=400, verbose_name='Вид деятельности')
    revenue_year = models.CharField(max_length=50, verbose_name='Выручка за год')
    profit_year = models.CharField(max_length=50, verbose_name='Доход за год')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='company')
