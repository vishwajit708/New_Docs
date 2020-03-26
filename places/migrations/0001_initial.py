# Generated by Django 3.0.3 on 2020-03-22 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('addr', models.TextField(blank=True, max_length=35, null=True)),
                ('open_time', models.TimeField(blank=True, null=True)),
                ('close_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('addr', models.TextField(blank=True, max_length=35, null=True)),
                ('open_time', models.TimeField(blank=True, null=True)),
                ('close_time', models.TimeField(blank=True, null=True)),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]