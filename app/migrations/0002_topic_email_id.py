# Generated by Django 5.0.3 on 2024-04-23 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='email_id',
            field=models.EmailField(default='ipl2024@gmail.com', max_length=100),
        ),
    ]
