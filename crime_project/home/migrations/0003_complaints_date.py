# Generated by Django 4.2.1 on 2023-05-16 05:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_complaints'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
