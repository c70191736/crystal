# Generated by Django 4.2.5 on 2023-10-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.URLField(blank=True, default=''),
        ),
    ]
