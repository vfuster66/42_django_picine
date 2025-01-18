# Generated by Django 5.0 on 2025-01-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ex02Movies',
            fields=[
                ('title', models.CharField(max_length=64, unique=True)),
                ('episode_nb', models.AutoField(primary_key=True, serialize=False)),
                ('opening_crawl', models.TextField(blank=True, null=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Movie (ex02)',
                'verbose_name_plural': 'Movies (ex02)',
                'db_table': 'ex02_movies',
            },
        ),
    ]
