# Django, Models
"""
Django — это мощный Python-фреймворк для создания сайтов и backend-приложений.
Он уже содержит готовые инструменты для работы с базой данных, авторизацией, 
админкой и API.

Модели - это python-классы, которые описывают таблицы в БД
"""
from django.db import models

# django автоматически создаст таблицу БД
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    

