# Generated by Django 4.1.4 on 2022-12-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_leadership_shumilino'),
    ]

    operations = [
        migrations.CreateModel(
            name='gas_potreb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('gas_potreb_doc', models.FileField(upload_to='gas_potreb/')),
                ('times', models.DateField()),
            ],
        ),
    ]