# Generated by Django 3.1.7 on 2021-02-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210227_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='simpleblog'),
        ),
    ]
