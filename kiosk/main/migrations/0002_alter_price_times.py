# Generated by Django 3.2.3 on 2021-05-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='times',
            field=models.DateField(),
        ),
    ]
