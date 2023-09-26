# Generated by Django 4.2.5 on 2023-09-22 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('folder', models.FileField(blank=True, default='', upload_to='folder')),
                ('amount', models.CharField(choices=[('free', 'free'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500'), ('600', '600'), ('7000', '700'), ('800', '800'), ('900', '900'), ('1000', '1000')], default='none', max_length=20)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
