from django.db import models

class Car(models.Model):
    name=models.CharField(max_length=256)
    color=models.CharField(max_length=256)
    price=models.IntegerField(default=0)
    image_url=models.CharField(max_length=256, default="")

    