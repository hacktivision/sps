from django.db import models
from django.conf import settings
from django.utils import timezone

class Faq(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete = models.CASCADE,
        verbose_name = 'Автор'
    )
    category = models.ForeignKey(
        'FaqCategory', 
        null = True, 
        on_delete = models.PROTECT,
        verbose_name ='Категория'
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    body = models.TextField(
        verbose_name = 'Описание'
    )
    create_date = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Создан'
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name = 'Обновлён'
    )
    published_date = models.DateTimeField(
        blank = True, 
        null = True,
        verbose_name = 'Публикация'
    )
    is_active = models.BooleanField(
        default = False,
        verbose_name = 'Активный'
    )
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('create_date',)
    
    def __str__(self):
        return self.title

class FaqCategory(models.Model):
    title = models.CharField(
        max_length = 32, 
        verbose_name = 'Название'
    )
    description = models.TextField(
        blank = True, 
        verbose_name = 'Описание'
    )
    
    class Meta:
        verbose_name = 'Категория вопросов'
        verbose_name_plural = 'Категории вопросов'
        
    def __str__(self):
        return self.title

class FaqTag(models.Model):
    pass

