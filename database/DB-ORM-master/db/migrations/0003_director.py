# Generated by Django 4.0.6 on 2022-08-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('debut', models.DateTimeField()),
                ('country', models.TextField()),
            ],
        ),
    ]
