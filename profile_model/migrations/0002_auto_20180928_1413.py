# Generated by Django 2.1.1 on 2018-09-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, to='comments_model.Comment'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contacts',
            field=models.ManyToManyField(blank=True, null=True, to='contact_model.Contact'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, to='course_model.Course'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='message',
            field=models.ManyToManyField(blank=True, null=True, to='message_model.Message'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='my_homework',
            field=models.ManyToManyField(blank=True, null=True, to='homework_model.HomeWork'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='saved_lessons',
            field=models.ManyToManyField(blank=True, null=True, to='test_student_model.Lesson'),
        ),
    ]
