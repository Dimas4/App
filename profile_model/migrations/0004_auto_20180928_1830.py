# Generated by Django 2.1.1 on 2018-09-28 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_model', '0003_auto_20180928_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='contacts',
            new_name='contact',
        ),
    ]