# Generated by Django 5.1.2 on 2024-11-14 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_orderdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdb',
            old_name='Message',
            new_name='Messages',
        ),
        migrations.RemoveField(
            model_name='orderdb',
            name='Ordernotes',
        ),
    ]
