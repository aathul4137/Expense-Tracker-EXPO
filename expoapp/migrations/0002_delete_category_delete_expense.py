# Generated by Django 5.0.4 on 2024-06-15 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expoapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]
