# Generated by Django 5.1.2 on 2024-11-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0005_rename_message_orderdb_messages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='Prod_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Cart Images'),
        ),
    ]
