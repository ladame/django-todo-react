# Generated by Django 4.2.4 on 2023-08-28 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='description',
            new_name='gambaran',
        ),
    ]
