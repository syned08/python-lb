from django.db import models


class Links(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    link_name = models.URLField(max_length=150, verbose_name='Название ссылки')
    count_visites = models.PositiveIntegerField(default=0, verbose_name='Кол-во переходов')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)
    author = models.ForeignKey('Authors', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ссылку'
        verbose_name_plural = 'Ссылки'
        ordering = ['-created_at', 'title']


class Categories(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Название')
    category_description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']


class Authors(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    second_name = models.CharField(max_length=150, verbose_name='Фамилия')
    country = models.CharField(max_length=150, verbose_name='Страна')
    age = models.PositiveIntegerField(verbose_name='Возраст')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'автора'
        verbose_name_plural = 'Авторы'
        ordering = ['first_name', 'second_name']
