# Generated by Django 5.0.2 on 2024-03-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_shared',
            field=models.BooleanField(default=False),
        ),
    ]