# Generated by Django 5.0.4 on 2024-05-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(max_length=50, verbose_name='Отчество'),
        ),
    ]