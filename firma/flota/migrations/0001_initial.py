# Generated by Django 3.1.3 on 2020-11-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=60)),
                ('nazwisko', models.CharField(max_length=60)),
                ('data_urodzenia', models.DateField()),
                ('zarobki', models.DecimalField(decimal_places=2, default=4000, max_digits=10)),
            ],
        ),
    ]
