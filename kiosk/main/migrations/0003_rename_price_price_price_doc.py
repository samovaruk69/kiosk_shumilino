# Generated by Django 3.2.3 on 2021-05-19 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_price_times'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='price',
            new_name='price_doc',
        ),
    ]
