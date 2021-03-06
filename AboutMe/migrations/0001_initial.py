# Generated by Django 3.0.3 on 2021-09-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('title', models.CharField(max_length=400, unique=True)),
                ('my_image', models.ImageField(blank=True, upload_to='photoes/aboutme/')),
            ],
        ),
    ]
