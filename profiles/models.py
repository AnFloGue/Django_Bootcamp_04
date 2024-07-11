from django.db import models


# python manage.py makemigrations

# python manage.py migrate

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    image = models.CharField(max_length=2083)
    
    def __str__(self):
        return self.name
