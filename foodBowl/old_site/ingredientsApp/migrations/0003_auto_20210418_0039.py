# Generated by Django 3.1.6 on 2021-04-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientsApp', '0002_auto_20210412_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='fats',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredDetails',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.TextField(default='Nameless'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='protein',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='sodium',
            field=models.IntegerField(default=0),
        ),
    ]
