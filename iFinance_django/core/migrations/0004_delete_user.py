# Generated by Django 5.0.4 on 2024-04-24 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_is_active_user_is_staff_user_last_login_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
