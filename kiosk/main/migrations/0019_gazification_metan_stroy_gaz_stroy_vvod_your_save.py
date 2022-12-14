# Generated by Django 4.1.3 on 2022-12-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_prikaz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gazification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Gazification_doc', models.FileField(upload_to='Gazification/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Metan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Metan_doc', models.FileField(upload_to='Metan/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stroy_gaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Stroy_gaz_doc', models.FileField(upload_to='Stroy_gaz/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stroy_vvod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Stroy_vvod_doc', models.FileField(upload_to='Stroy_vvod/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Your_save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Your_save_doc', models.FileField(upload_to='Your_save/')),
                ('times', models.DateField()),
            ],
        ),
    ]
