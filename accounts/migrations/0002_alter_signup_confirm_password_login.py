# Generated by Django 4.2.3 on 2023-07-08 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='confirm_password',
            field=models.CharField(default='use same password', max_length=50),
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logins', to='accounts.signup')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logging', to='accounts.signup')),
            ],
        ),
    ]