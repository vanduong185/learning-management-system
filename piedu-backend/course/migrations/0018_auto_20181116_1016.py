# Generated by Django 2.1 on 2018-11-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_auto_20181116_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='session_end',
            field=models.CharField(max_length=5, null=True, verbose_name='Start Session'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='session_start',
            field=models.CharField(max_length=5, null=True, verbose_name='Start Session'),
        ),
    ]