# Generated by Django 4.2.5 on 2023-09-24 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, default='', upload_to='file'),
        ),
    ]
