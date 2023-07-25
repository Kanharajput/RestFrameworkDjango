from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Book(models.Model):
    book_title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_title

