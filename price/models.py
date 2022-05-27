from django.db import models


class Card(models.Model):
    price = models.PositiveIntegerField('Цена')
    description = models.CharField('Описание', max_length=200)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'


class Service(models.Model):
    title = models.CharField('Услуга', max_length=200)
    old_price = models.PositiveIntegerField('Старая цена')
    new_price = models.PositiveIntegerField('Новая цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
