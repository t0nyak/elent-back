# Generated by Django 2.2.6 on 2020-04-15 06:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200104_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=120)),
                ('type', models.IntegerField(choices=[(0, 'UserProfile'), (1, 'BlogPost'), (2, 'ShopItem')])),
            ],
        ),
    ]