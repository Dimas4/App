# Generated by Django 2.1.1 on 2018-09-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_model', '0002_contact_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
