# Admin (Админка)
"""
Django имеет встроенную админ-панель.

Можно управлять:

пользователями
товарами
постами
заказами
любыми моделями
"""

# подключение модели к админке
from django.contrib import admin

from .models import User

admin.site.register(User)

"""
ШАГ 1 — Создаем папку проекта
Создай папку: DJANGO
cd Desktop\PythonProjects\DJANGO

ШАГ 2 — Создаем виртуальное окружение
py -m venv .venv

ШАГ 3 — Активируем venv
.venv\Scripts\activate

ШАГ 4 — Устанавливаем Django
pip install django

Проверка: pip list
Там должен быть: Django

ШАГ 5 — Создаем Django проект
Выполняем:

django-admin startproject config .

Точка . обязательна.

После этого структура должна быть ТАКАЯ
DJANGO/
│
├── .venv/
├── manage.py
└── config/
    ├── settings.py
    ├── urls.py
    └── ...

ШАГ 6 — Делаем миграции
py manage.py migrate

ШАГ 7 — Создаем админа
py manage.py createsuperuser

Django спросит:

Username:
Email:
Password:

ШАГ 9 — Запускаем сервер
py manage.py runserver

Открой в браузере:
http://127.0.0.1:9000/admin
Войди через superuser

Используй:

Username → который создала admin
Password → который вводила admin123
"""