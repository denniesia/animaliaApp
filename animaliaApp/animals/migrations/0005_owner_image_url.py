# Generated by Django 5.2 on 2025-04-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_remove_animal_age_remove_owner_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
