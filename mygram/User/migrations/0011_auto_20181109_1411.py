# Generated by Django 2.1.3 on 2018-11-09 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_auto_20181109_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileimage',
            name='id',
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='User.Profile', unique=True, verbose_name='Пользователь'),
        ),
    ]
