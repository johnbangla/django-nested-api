# Generated by Django 3.0.6 on 2020-08-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactapp', '0003_iimage_aimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iimage',
            name='aimage',
            field=models.ImageField(blank=True, default=None, upload_to='photos'),
        ),
    ]
