# Generated by Django 4.2.6 on 2023-10-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_employee_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default='2023-10-25'),
            preserve_default=False,
        ),
    ]
