# Generated by Django 2.0 on 2017-12-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='photo',
            field=models.ImageField(upload_to='app/static/Instagram/images'),
        ),
    ]