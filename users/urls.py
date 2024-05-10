from django.urls import path, include
from django.views.generic import TemplateView

from users.views import RegisterView, AddPassport, AddCompany

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('passport/', AddPassport.as_view(), name='passport'),
    path('company/', AddCompany.as_view(), name='company'),
    path('', include('django.contrib.auth.urls'))
]
