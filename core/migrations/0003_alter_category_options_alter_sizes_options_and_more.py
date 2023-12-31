# Generated by Django 4.0 on 2023-07-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_sizes_product_category_product_sizes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория товара', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='sizes',
            options={'verbose_name': 'Размер', 'verbose_name_plural': 'Размеры'},
        ),
        migrations.AddField(
            model_name='product',
            name='compound',
            field=models.CharField(default='Хорошая ткань', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='textile',
            field=models.CharField(default='Хорошая ткань', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sizes',
            name='text_name',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Текстовый размер'),
        ),
    ]
