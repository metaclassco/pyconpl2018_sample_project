from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    manufacturer = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.category)
