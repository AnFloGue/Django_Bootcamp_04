from django.db import models
from django.conf import settings

# python manage.py makemigrations
# python manage.py migrate

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
