# Generated by Django 2.0.5 on 2018-07-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0005_auto_20180706_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='img_file',
            field=models.ImageField(upload_to='images'),
        ),
    ]