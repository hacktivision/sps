# Generated by Django 3.1.7 on 2021-03-02 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210302_2056'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StatusTask',
            new_name='TaskStatus',
        ),
    ]
