# Generated by Django 4.2 on 2023-06-18 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialist',
            old_name='image',
            new_name='personal_image',
        ),
    ]
