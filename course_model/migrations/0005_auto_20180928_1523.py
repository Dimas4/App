# Generated by Django 2.1.1 on 2018-09-28 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_model', '0004_auto_20180928_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='direction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='direction_course_model.Direction'),
            preserve_default=False,
        ),
    ]
