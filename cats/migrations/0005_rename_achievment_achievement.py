# Generated by Django 3.2 on 2024-09-21 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_cat_achievements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Achievment',
            new_name='Achievement',
        ),
    ]
