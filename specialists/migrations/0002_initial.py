# Generated by Django 4.2 on 2023-06-07 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('specialists', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialistreviews',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialist_reviews', to='users.client'),
        ),
        migrations.AddField(
            model_name='specialistreviews',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='users.specialist'),
        ),
        migrations.AlterUniqueTogether(
            name='specialistreviews',
            unique_together={('client', 'specialist')},
        ),
    ]
