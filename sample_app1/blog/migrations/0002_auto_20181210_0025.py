# Generated by Django 2.1.4 on 2018-12-10 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='craeted',
            new_name='created',
        ),
    ]
