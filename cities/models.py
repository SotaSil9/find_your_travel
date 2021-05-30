from django.db import models
from django.urls import reverse


class City(models.Model):  # создание базы уникальных названий
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):  # отображение имени в админке
        return self.name

    class Meta:  # отображение полей модели, сортировка по имени
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})

