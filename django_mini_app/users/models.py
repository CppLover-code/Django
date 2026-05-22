from django.db import models

# Миграции — это система изменения базы данных в Django.
class User(models.Model):                       # Наследование от Django модели.
    # поля
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name                        # объект отображается в admin panel.
    

"""
Далее создаем миграции
py manage.py makemigrations

Django создаст файл:
users/migrations/0001_initial.py

Применяем миграции
py manage.py migrate
Теперь таблица реально создается в базе данных SQLite.
"""