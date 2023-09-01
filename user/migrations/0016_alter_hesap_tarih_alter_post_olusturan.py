# Generated by Django 4.1.7 on 2023-08-31 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0015_rename_begenenler_post_kaydedenler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hesap',
            name='tarih',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='olusturan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]