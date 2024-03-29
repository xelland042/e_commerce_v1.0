# Generated by Django 5.0.2 on 2024-02-29 11:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('about_product', models.TextField()),
                ('in_discount', models.BooleanField(default=False)),
                ('discount_percentage', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('base_specifications', models.JSONField(blank=True, null=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('place', models.IntegerField()),
                ('main_image', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('specification', models.JSONField()),
                ('quantity', models.BigIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
