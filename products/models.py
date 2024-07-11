from django.db import models

# python manage.py makemigrations

# python manage.py migrate


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
