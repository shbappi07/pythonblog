# Generated by Django 4.1.7 on 2023-04-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('featured_image', models.ImageField(upload_to='uploads/')),
                ('tags', models.CharField(max_length=200)),
                ('featured', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('mod_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
