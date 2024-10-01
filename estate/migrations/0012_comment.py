# Generated by Django 5.1.1 on 2024-09-27 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0011_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=None, max_length=50)),
                ('image', models.ImageField(upload_to='image')),
                ('comment', models.TextField(blank=None, max_length=300)),
                ('profession', models.CharField(blank=None, max_length=50)),
            ],
        ),
    ]
