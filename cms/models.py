from django.db import models


class Slider(models.Model):
    img = models.ImageField(upload_to='slider_img/')
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст')
    css = models.CharField('CSS', max_length=200, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ('title',)
