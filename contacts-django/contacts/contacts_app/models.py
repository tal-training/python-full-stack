from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=256)
    phone=models.CharField(max_length=256)
    email=models.CharField(max_length=256)
    address=models.CharField(max_length=256)