from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name
