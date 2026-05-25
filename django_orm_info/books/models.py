from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title, self.author, self.category}"