# Generated by Django 4.1.7 on 2023-08-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_post_begenenler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='begenenler',
        ),
        migrations.AddField(
            model_name='post',
            name='begenenler',
            field=models.ManyToManyField(to='user.hesap'),
        ),
    ]