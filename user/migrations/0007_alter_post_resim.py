# Generated by Django 4.1.7 on 2023-08-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_post_olusturan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resim',
            field=models.FileField(null=True, upload_to='pin/'),
        ),
    ]
