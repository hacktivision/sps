from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

from djmoney.models.fields import MoneyField
from django_editorjs import EditorJsField

# Project
class Project(models.Model):
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete = models.CASCADE,
        verbose_name = 'Автор'
    )
    
    manager = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.PROTECT, 
        related_name='project_manager',
        verbose_name = 'Менеджер проекта'
    )
    
    customer = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.PROTECT, 
        related_name='project_customer',
        verbose_name = 'Заказчик'
    )
    
    performer = models.ForeignKey(
        User, 
        null=True, 
        on_delete=models.PROTECT, 
        related_name='project_performer',
        verbose_name = 'Исполнттель'
    )
    
    type_project = models.ForeignKey(
        'TypeProject', 
        null=True, 
        on_delete=models.PROTECT, 
        verbose_name='Тип проекта'
    )
    
    categories_project = models.ManyToManyField(
        'CategoryProject',
        verbose_name="Категории"
    )
    
    status_project = models.ForeignKey(
        'StatusProject', 
        null=True, 
        on_delete=models.PROTECT, 
        verbose_name='Статус'
    )
    
    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название'
    )
    
    description = models.TextField(
        blank=True, 
        verbose_name = "Описание"
    )
    
    technical_task = EditorJsField(
        blank=True, 
        verbose_name = "Техническое задание"
    )
    
    contract = models.URLField(
        max_length=255,
        db_index=True,
        verbose_name='Ссылка на договор'
    )
    
    total_budget = MoneyField(
        max_digits=14, 
        decimal_places=2, 
        default_currency='RUB',
        default=0,
        verbose_name='Бюджет проекта'
    )
    
    spent_budget = MoneyField(
        max_digits=14, 
        decimal_places=2, 
        default_currency='RUB',
        default=0,
        verbose_name='Расход'
    )
    
    balance_budget = MoneyField(
        max_digits=14, 
        decimal_places=2, 
        default_currency='RUB',
        default=0,
        verbose_name='Остаток'
    )
    
    cteated_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Создан'
    )
    
    update_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Обновлён'
    )
    
    published_date = models.DateTimeField(
        blank = True, 
        null = True,
        verbose_name = 'Публикация'
    )
    
    start_date = models.DateTimeField(
        blank=True,
        null = True,
        verbose_name='Дата старта'
    )
    
    completed_date = models.DateTimeField(
        blank=True,
        verbose_name='Дата завершения',
    )
    
    priority = models.PositiveSmallIntegerField(
        default=False,
        verbose_name='Приоритет',
    )
    
    is_active = models.BooleanField(
        default=True, 
        verbose_name='Активный'
    )
    
    is_done = models.BooleanField(
        default=False, 
        verbose_name='Реализован'
    )
    
    class Meta:
        verbose_name='Проект'
        verbose_name_plural='Проекты'
        ordering=['cteated_date']
        
    def __str__(self):
        return self.title
    
# Category project
class CategoryProject(models.Model):
    title = models.CharField(
        max_length=128, 
        db_index=True, 
        verbose_name='Название'
    )
    
    description = models.TextField(
        blank=True, 
        verbose_name="Описание"
    )
    
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title']
        
    def __str__(self):
        return self.title    

# Type priject
class TypeProject(models.Model):
    title = models.CharField(
        max_length=128,
        db_index=True,
        verbose_name='Название'
    )
    
    description = models.TextField(
        blank=True, 
        verbose_name="Описание"
    )
    
    class Meta:
        verbose_name='Тип проекта'
        verbose_name_plural='Типы проектов'
        ordering=['title']
        
    def __str__(self):
        return self.title
    
# Status project
class StatusProject(models.Model):
    title = models.CharField(
        max_length=32, 
        db_index=True, 
        verbose_name='Назвение'
    )
    
    class Meta:
        verbose_name='Статус проекта'
        verbose_name_plural='Статусы проекта'
        ordering=['title']
        
    def __str__(self):
        return self.title

# Task
class TaskProject(models.Model):
    project = models.ForeignKey(
        'Project', 
        null=True, 
        on_delete=models.PROTECT, 
        verbose_name='Проект'
    )
    
    title = models.CharField(
        max_length=128,
        db_index=True, 
        verbose_name='Назвение'
    )
    
    description = models.TextField(
        blank=True, 
        verbose_name='Описание'
    )
    
    total_cost = MoneyField(
        max_digits=14, 
        decimal_places=2, 
        default_currency='RUB',
        default=0,
        verbose_name='Стоимость задачи'
    )
    
    cteated_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Создана'
    )
    
    update_date = models.DateTimeField(
        auto_now=True, 
        verbose_name='Обновленна'
    )
    
    completed_date = models.DateTimeField(
        blank=True,
        verbose_name='Дата завершения',
    )
    
    status_task = models.ForeignKey(
        'StatusTask', 
        null=True, 
        on_delete=models.PROTECT, 
        verbose_name='Статус'
    )
    
    is_active = models.BooleanField(
        default = True, 
        verbose_name='Активная'
    )
    
    is_done = models.BooleanField(
        default = False, 
        verbose_name='Реализованная'
    )
    
    is_priority = models.BooleanField(
        default = False, 
        verbose_name='В приоритете'
    )
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['cteated_date']
        
    def __str__(self):
        return self.title
    
# Task status
class StatusTask(models.Model):
    title = models.CharField(
        max_length=32, 
        db_index=True, 
        verbose_name='Назвение',
    )
    
    class Meta:
        verbose_name='Статус задачи'
        verbose_name_plural='Статусы задачи'
        ordering=['title']
        
    def __str__(self):
        return self.title


# Checklist
class CheckList(models.Model):
    
    task = models.ForeignKey(
        'TaskProject', 
        null=True, 
        on_delete=models.PROTECT, 
        verbose_name='Задача'
    )
    
    title = models.CharField(
        max_length=128,
        db_index=True,
        verbose_name='Назвение'
    )
    
    cteated_date = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Создан'
    )
    
    update_date = models.DateTimeField(
        auto_now=True, 
        verbose_name='Обновлён'
    )
    
    completed_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата завершения',
    )

    is_active = models.BooleanField(
        default = True, 
        verbose_name='Активный'
    )
        
    is_done = models.BooleanField(
        default=False, 
        verbose_name='Выполнен'
    )
    
    class Meta:
        verbose_name='Элемент списка'
        verbose_name_plural='Активный список'
        ordering=['cteated_date']
        
    def __str__(self):
        return self.title
