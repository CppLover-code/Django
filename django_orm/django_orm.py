"""
ORM (Object Relational Mapping) — это система, которая позволяет работать с базой данных через 
Python-код, а не писать SQL вручную.

Пример:
users = User.objects.all()

вместо:
SELECT * FROM users;
"""
#********************************************************
# RELATIONS
"""
В Django есть 3 основные связи:

Связь	            Django	            Пример
Один к одному	    OneToOneField	    Пользователь ↔ Профиль
Один ко многим	    ForeignKey	        Категория → Товары
Многие ко многим	ManyToManyField	    Студенты ↔ Курсы
"""
"""
ForeignKey (Один ко многим)
Пример: Категории и товары
models.py
from django.db import models
"""

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    def __str__(self):
        return self.title

"""
Что означает ForeignKey
category = models.ForeignKey(...)

Каждый товар принадлежит одной категории.

Но одна категория может иметь много товаров.

on_delete

Что делать при удалении категории.

CASCADE
on_delete=models.CASCADE

Удалится и категория, и все товары внутри неё.
"""
#********************************************************
# МИГРАЦИИ
"""
python manage.py makemigrations
python manage.py migrate
Работа через shell
python manage.py shell
"""
#********************************************************
# СОЗДАНИЕ ОБЪЕКТОВ
from shop.models import Category, Product

cat = Category.objects.create(name="Phones")

Product.objects.create(
    title="iPhone",
    price=3000,
    category=cat
)
#********************************************************
# ПОЛУЧЕНИЕ СВЯЗАННЫХ ОБЪЕКТОВ 
# 
# От товара к категории
product = Product.objects.first()

print(product.category)

# От категории к товарам
cat.products.all()
""" Потому что:

related_name="products" """

#******************************
# OneToOneField
# Пример: Профиль пользователя

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField()

""" Смысл

У одного пользователя один профиль.

profile.user
user.profile """  

#******************************
# ManyToManyField
# Пример: Студенты и курсы

class Course(models.Model):
    title = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)

    courses = models.ManyToManyField(
        Course
    )

"""
Работа с ManyToMany: 

Добавить курс
student.courses.add(course)

Получить курсы
student.courses.all()

Получить студентов курса
course.student_set.all()
"""

# ОПТМИЗАЦИЯ ORM
# ПРОБЛЕМА
"""
Проблема N+1 Query

Допустим:

products = Product.objects.all()

for product in products:
    print(product.category.name)

Что происходит - 1 запрос на товары.

И ещё отдельный запрос на категорию каждого товара.
Если 100 товаров → 101 SQL запрос.
Это ПЛОХО.

select_related()

Используется для:
ForeignKey
OneToOneField
"""
# Правильно
products = Product.objects.select_related("category") # Теперь будет только 1 SQL запрос.

for product in products:
    print(product.category.name)

# ************************************************
"""
prefetch_related()

Используется для:

ManyToMany
reverse ForeignKey
"""
# Пример
categories = Category.objects.prefetch_related("products")

for category in categories:
    print(category.products.all())

"""
Разница
Метод	                Для чего
select_related()	    ForeignKey / OneToOne
prefetch_related()	    ManyToMany / reverse FK
"""

Product.objects.only("title")   # Загружает только нужные поля.
Product.objects.values("title", "price")    # Возвращает словари вместо объектов.
"""
Result:
[
    {"title": "iPhone", "price": 3000}
]
"""
# лучше
Product.objects.count() 
# чем
len(Product.objects.all())

Product.objects.filter(price=100).exists()  # Проверка существования:

# Агрегации
from django.db.models import Avg

Product.objects.aggregate(
    Avg("price")
)

# annotate() Добавляет вычисляемые поля.

from django.db.models import Count

Category.objects.annotate(
    products_count=Count("products")
)
