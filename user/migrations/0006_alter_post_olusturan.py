# Generated by Django 4.1.7 on 2023-08-03 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0005_remove_post_fiyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='olusturan',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
