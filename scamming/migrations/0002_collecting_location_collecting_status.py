# Generated by Django 4.2.3 on 2023-07-07 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scamming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collecting',
            name='location',
            field=models.CharField(default='Kigali or other', max_length=20),
        ),
        migrations.AddField(
            model_name='collecting',
            name='status',
            field=models.CharField(default='employed or student or unemployed', max_length=50),
        ),
    ]
