from django.db import models

class Articles(models.Model):
    title = models.CharField('Нзвание', max_length=50) # строка из 250 симоволов? максимальное число вводимых символов 50
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья') # возможен ввод большого количества символов
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'