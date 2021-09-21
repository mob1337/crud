from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50,default='')
    author = models.CharField(max_length=50, default='')
    isbn = models.CharField(max_length=50, default='')
    price = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.name
        return self.author
        return self.isbn
        return self.price
    
