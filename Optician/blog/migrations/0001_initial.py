# Generated by Django 5.0.7 on 2024-09-22 18:49

import django.db.models.deletion
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
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='max 100 characters', max_length=100, verbose_name='Title of the blog cart')),
                ('image', models.ImageField(upload_to='', verbose_name='Image of the blog cart')),
                ('description', models.TextField(verbose_name='Text of the blog cart')),
                ('description_en', models.TextField(null=True, verbose_name='Text of the blog cart')),
                ('description_az', models.TextField(null=True, verbose_name='Text of the blog cart')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Comment name')),
                ('email', models.EmailField(max_length=254, verbose_name='Comment email')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_of_th_blog', to='blog.blog')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'All comments',
            },
        ),
    ]
