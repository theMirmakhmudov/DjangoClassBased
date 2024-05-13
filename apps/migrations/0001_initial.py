# Generated by Django 5.0.6 on 2024-05-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('jobs', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default='default-user.png', help_text='Rasm kiritmaslik mumkin', null=True, upload_to='images/')),
            ],
        ),
    ]
