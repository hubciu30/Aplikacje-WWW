# Generated by Django 3.1.3 on 2020-12-16 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flota', '0003_auto_20201209_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochod',
            name='wlasciciel_uzytkownik',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='samochody', to='auth.user'),
            preserve_default=False,
        ),
    ]
