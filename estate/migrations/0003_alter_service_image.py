# Generated by Django 5.1.1 on 2024-09-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_alter_service_description_alter_service_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
