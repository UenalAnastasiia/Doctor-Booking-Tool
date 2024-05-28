# Generated by Django 5.0.6 on 2024-05-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('title', models.IntegerField(choices=[(1, 'Dr.'), (2, 'Prof. Dr.'), (3, 'Dr. rer. nat.')])),
                ('speciality', models.IntegerField(choices=[(1, 'Allgemeinmedizin'), (2, 'Radiologe'), (3, 'Hautarzt')])),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
    ]
