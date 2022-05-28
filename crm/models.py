from django.db import models


class Status(models.Model):
    status = models.CharField('Название статуса', max_length=200)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    created_at = models.DateTimeField('Время заказа', auto_now=True)
    name = models.CharField('Имя', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    created_at = models.DateTimeField('Дата создания', auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка от')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
