# Generated by Django 4.2.3 on 2023-07-08 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_login_password_alter_login_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
