# Generated by Django 5.0.4 on 2024-04-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_userprofile_bank_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bank_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
