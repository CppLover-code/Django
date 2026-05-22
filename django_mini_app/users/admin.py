from django.contrib import admin
from .models import User

admin.site.register(User)       # показать модель User в админке.

# запускаем сервер
# py manage.py runserver 9000
# открываем админку http://127.0.0.1:9000/admin

"""
Админка позволяет:
- добавлять пользователей
- редактировать
- удалять
- смотреть данные БД

"""

