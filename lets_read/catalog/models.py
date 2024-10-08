from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    info = models.TextField()

    def __str__(self):
        return f"{self.name} by {self.author} in {self.year}"
