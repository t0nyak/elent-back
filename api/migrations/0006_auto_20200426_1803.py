# Generated by Django 2.2.6 on 2020-04-26 18:03

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200426_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/elent/back-admin/media/images'), upload_to=''),
        ),
    ]