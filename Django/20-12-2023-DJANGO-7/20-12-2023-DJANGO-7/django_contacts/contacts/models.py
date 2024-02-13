from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=256)
    phone=models.CharField(max_length=256)
    email = models.EmailField(default="")

    def __str__(self) -> str:
        return f"{self.name}:{self.phone}"
    
class User(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=12)
