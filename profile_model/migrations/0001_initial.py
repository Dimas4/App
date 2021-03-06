# Generated by Django 2.1.1 on 2018-09-28 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_model', '0001_initial'),
        ('contact_model', '0001_initial'),
        ('test_student_model', '0001_initial'),
        ('homework_model', '0001_initial'),
        ('message_model', '0001_initial'),
        ('comments_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='')),
                ('about_me', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.ManyToManyField(to='comments_model.Comment')),
                ('contacts', models.ManyToManyField(to='contact_model.Contact')),
                ('course', models.ManyToManyField(to='course_model.Course')),
                ('message', models.ManyToManyField(to='message_model.Message')),
                ('my_homework', models.ManyToManyField(to='homework_model.HomeWork')),
                ('saved_lessons', models.ManyToManyField(to='test_student_model.Lesson')),
            ],
        ),
    ]
