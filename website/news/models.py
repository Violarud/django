from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=120)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Содержание')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'News": {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'