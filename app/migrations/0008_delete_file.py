# Generated by Django 4.2.5 on 2023-09-30 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_phonetype_file_remove_phonenumber_dude_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]
