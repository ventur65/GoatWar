# Generated by Django 3.0 on 2019-12-16 17:45

import backend.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20191216_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goat',
            name='image',
            field=models.ImageField(blank=True, height_field='_height', upload_to=backend.models.path_to_image, width_field='_width'),
        ),
        migrations.AlterField(
            model_name='goat',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='date published'),
        ),
    ]
