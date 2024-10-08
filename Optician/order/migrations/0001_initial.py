# Generated by Django 5.0.7 on 2024-09-22 18:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_basket', to='product.productversion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_basket', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'BasketItem',
                'verbose_name_plural': 'BasketItems',
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_basket_item', to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(related_name='basket_item', to='order.basketitem')),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Baskets',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ManyToManyField(related_name='product_wishlist', to='product.productversion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_wishlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'WishList',
                'verbose_name_plural': 'WishLists',
            },
        ),
    ]
