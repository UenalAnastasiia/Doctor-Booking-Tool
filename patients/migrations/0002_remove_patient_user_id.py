# Generated by Django 5.0.6 on 2024-05-28 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user_id',
        ),
    ]
