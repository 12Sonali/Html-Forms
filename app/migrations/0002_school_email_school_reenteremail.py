# Generated by Django 4.2.7 on 2024-01-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.EmailField(default='hey@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='school',
            name='reenteremail',
            field=models.EmailField(default='hey@gmail.com', max_length=254),
        ),
    ]
