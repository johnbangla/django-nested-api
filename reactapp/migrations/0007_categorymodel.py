# Generated by Django 3.1 on 2020-08-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactapp', '0006_iimage_bimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('backgroundColor', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
    ]
