# Generated by Django 5.0.6 on 2024-05-13 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]