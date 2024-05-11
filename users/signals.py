from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User, PersonalAccount


@receiver(post_save, sender=User)
def test_view(sender, instance, created, **kwargs):
    if created:
        PersonalAccount.objects.create(user=instance)
        send_mail('Приветственное сообщение', 'Приветствуем Вас на нашем сайте',
                  settings.EMAIL_HOST_USER, [instance.email])




