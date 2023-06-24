# Generated by Django 4.2 on 2023-06-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('REQUESTED', 'Requested'), ('ACCEPTED', 'Accepted'), ('DISABLED', 'Disabled'), ('ENABLED', 'Enabled')], default='DISABLED', max_length=9),
        ),
    ]
