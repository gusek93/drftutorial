# Generated by Django 4.0.1 on 2022-01-10 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_active_user_is_admin_user_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
    ]