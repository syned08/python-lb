from django.db import models

class Links(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    link_name = models.URLField(max_length=150, verbose_name='Название ссылки')
    count_visites = models.PositiveIntegerField(default=0, verbose_name='Кол-во переходов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ссылку'
        verbose_name_plural = 'Ссылки'
        ordering = ['-created_at', 'title']
