# Generated by Django 5.1.1 on 2024-10-16 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(max_length=10, verbose_name='phone_number'),
        ),
    ]
