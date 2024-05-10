from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import User, Passport


class UserCreateForm(UserCreationForm):

    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'patronymic', 'email', 'role', 'username', ]
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'email': '@email',
            'username': 'Логин',
            'role': 'Категория',
        }


class PassportCreateForm(forms.ModelForm):
    class Meta:
        model = Passport
        exclude = ['user']
        labels = {
            'series': 'Серия',
            'number': 'Номер',
            'issued': 'Выдан',
            'date_of_issued': 'Дата выдачи',
            'department_code': 'Код подразделения',
            "date_of_birth": 'Дата рождения',
            'place_of_birth': 'Место рождения',
            'registration_address': 'Место регистрации'
        }
