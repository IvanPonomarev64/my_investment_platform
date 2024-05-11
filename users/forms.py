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
        fields = ['series', 'number', 'issued', 'date_of_issued', 'department_code',
                  "date_of_birth", 'place_of_birth', 'registration_address']
        widgets = {
            'date_of_issued': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }
