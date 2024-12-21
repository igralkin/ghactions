from django.db import models


class Module(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    education_time = models.IntegerField(null=True, blank=True, verbose_name='Срок обучения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'
