# Generated by Django 5.0.4 on 2024-05-07 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passport', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personalaccount',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL),
        ),
    ]
