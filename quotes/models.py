from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.text