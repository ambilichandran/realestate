# Generated by Django 5.1.1 on 2024-09-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0009_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
