from typing import Iterable, Optional
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from core.management.commands.bot import bot

class Product(models.Model):
    title = models.CharField('Заголовок', max_length=140)
    price = models.IntegerField('Цена продукта')
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='images')

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
    phone_number = PhoneNumberField()
    confirmed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Запрос на перезвон'
        verbose_name_plural = 'Запросы на перезвон'
    
    def __str__(self) -> str:
        return str(self.phone_number)