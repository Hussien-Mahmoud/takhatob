# Generated by Django 4.2 on 2023-06-18 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0003_specialistcertifications'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialistcertifications',
            old_name='image',
            new_name='certification_image',
        ),
    ]
