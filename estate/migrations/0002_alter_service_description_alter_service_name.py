# Generated by Django 5.1.1 on 2024-09-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(blank=None, max_length=100),
        ),
    ]
