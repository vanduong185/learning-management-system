# Generated by Django 2.1 on 2018-11-06 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20181031_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Course Category')),
            ],
            options={
                'verbose_name': 'Catergory',
                'verbose_name_plural': 'Categories',
                'db_table': 'course_category',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Subject')),
                ('avatar', models.ImageField(null=True, upload_to='', verbose_name='Avatar')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
                'db_table': 'subject',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='class',
            name='course_id',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AddField(
            model_name='class',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.CourseCategory', verbose_name='Course Category'),
        ),
        migrations.AddField(
            model_name='class',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Subject', verbose_name='Subject'),
        ),
    ]