# Generated by Django 3.0.6 on 2020-08-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactapp', '0004_auto_20200808_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iimage',
            name='aimage',
            field=models.ImageField(default='default.jpg', upload_to='photos'),
        ),
    ]
