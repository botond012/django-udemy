# Generated by Django 4.0.1 on 2022-02-01 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
