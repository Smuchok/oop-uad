from django.db import models

# Create your models here.

class Titles(models.Model):
    title = models.CharField('Назва', max_length=50, default='Без назви')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст статті')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
