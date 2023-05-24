# Generated by Django 4.2 on 2023-05-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_center_is_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='excerpt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='specialist',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='image',
            field=models.ImageField(default='images/centers/default-placeholder.png', upload_to='images/specialists/profile_images/'),
        ),
    ]
