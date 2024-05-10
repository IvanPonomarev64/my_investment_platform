from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserCreateForm, PassportCreateForm
from users.models import Company


class RegisterView(CreateView):
    form_class = UserCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class AddPassport(CreateView):
    form_class = PassportCreateForm
    template_name = 'registration/passport.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddCompany(CreateView):
    model = Company
    template_name = 'registration/company.html'
    success_url = reverse_lazy('home')
    fields = ['name', 'inn', 'kpp', 'ogrn', 'address', 'type', 'revenue_year', 'profit_year']

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        send_mail('Приветственное сообщение', 'Приветствуем Вас на нашем сайте',
                  settings.EMAIL_HOST_USER, [self.request.user.email])
        return HttpResponseRedirect(self.success_url)













