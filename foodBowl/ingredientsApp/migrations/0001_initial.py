# Generated by Django 3.2 on 2021-04-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('directions', models.TextField()),
                ('fats', models.FloatField()),
                ('protein', models.FloatField()),
                ('calories', models.FloatField()),
                ('sodium', models.FloatField()),
                ('desc', models.TextField(default=None)),
                ('ingredDetails', models.TextField()),
                ('categories', models.ManyToManyField(to='ingredientsApp.Category')),
            ],
        ),
    ]
