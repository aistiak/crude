# Generated by Django 2.0.5 on 2018-07-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0003_auto_20180706_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='img_file',
            field=models.FileField(upload_to=''),
        ),
    ]
