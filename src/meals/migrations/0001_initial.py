# Generated by Django 3.2.11 on 2022-01-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('describtion', models.TextField(max_length=500)),
                ('people', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preperation_time', models.IntegerField()),
                ('image', models.ImageField(upload_to='meals/')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'meal',
                'verbose_name_plural': 'meals',
            },
        ),
    ]
