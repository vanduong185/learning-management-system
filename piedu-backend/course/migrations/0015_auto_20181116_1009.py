# Generated by Django 2.1 on 2018-11-16 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20181111_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='code',
            field=models.CharField(default='', max_length=25, unique=True, verbose_name="Class's Code"),
        ),
        migrations.AlterField(
            model_name='subject',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects_set', to='course.CourseCategory', verbose_name='Course Category'),
        ),
    ]
