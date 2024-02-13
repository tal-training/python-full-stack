from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=256)
    phone=models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.name}:{self.phone}"