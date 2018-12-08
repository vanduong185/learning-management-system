# Generated by Django 2.1 on 2018-11-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_auto_20181116_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day_of_week',
            field=models.CharField(max_length=3, verbose_name='Day Of Week'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='session_end',
            field=models.CharField(max_length=3, null=True, verbose_name='End Session'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='session_start',
            field=models.CharField(max_length=3, null=True, verbose_name='Start Session'),
        ),
    ]