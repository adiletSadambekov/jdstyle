from typing import Iterable, Optional
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from core.management.commands.bot import bot

class Category(models.Model):
    name = models.CharField('Название', max_length=60)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'

    def __str__(self) -> str:
        return f'{self.int_name} - {self.text_name}'


class Sizes(models.Model):
    text_name = models.CharField(verbose_name='Текстовый размер', max_length=6, null=True, blank=True)
    int_name = models.IntegerField(verbose_name='Числовой размер')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
    
    def __str__(self) -> str:
        return f'{self.int_name} - {self.text_name}'



class Product(models.Model):
    title = models.CharField('Заголовок', max_length=140)
    price = models.IntegerField('Цена продукта')
    description = models.TextField('Описание', null=True, blank=True)
    image = models.ImageField(upload_to='images')
    textile = models.CharField(max_length=60)
    compound = models.CharField(max_length=120)
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    sizes = models.ManyToManyField(Sizes, related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    
    def __str__(self) -> str:
        return self.title


# class ProductPhoto(models.Model):
#     product = models.(Product, models.CASCADE, related_name='photos')
#     photo = models.ImageField(upload_to='images')
#     is_main = models.BooleanField('Главное фото', default=False)

#     def save(self, *args, **kwargs) -> None:
#         if self.is_main == True:
#             photos = ProductPhoto.objects.filter(product=self.product, is_main=True)
#             for p in photos:
#                 p.is_main = False
#                 p.save()
#         return super().save(*args, **kwargs)

#     class Meta:
#         verbose_name = 'Фото продукта'
#         verbose_name_plural = 'Фото продуктов'
#         # unique_together = ['product', 'is_']
    
    # def __str__(self) -> str:
    #     return self.product.title


class ToNotification(models.Model):
    tg_id = models.CharField('id в телеграмме',max_length=90)
    class Meta:
        verbose_name = 'Получатель опавещения'
        verbose_name_plural = 'Получатели опавещений'


class ApplicationCall(models.Model):
    name = models.TextField()
    phone_number = models.CharField(max_length=16)
    confirmed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Запрос на перезвон'
        verbose_name_plural = 'Запросы на перезвон'
    
    def __str__(self) -> str:
        return str(self.phone_number)