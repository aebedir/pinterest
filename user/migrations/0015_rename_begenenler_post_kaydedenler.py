# Generated by Django 4.1.7 on 2023-08-07 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_hesap_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='begenenler',
            new_name='kaydedenler',
        ),
    ]
