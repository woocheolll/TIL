# Generated by Django 4.0.6 on 2022-08-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
    ]