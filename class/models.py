from django.db import models
from django.contrib.auth.models import User

# Create your models here.


choose_class = (('1', 'form1'),('2', 'form2'),('3','form3'),('4', 'shs'))

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=10, null=True)
    Class = models.CharField(choices=choose_class, default=2, max_length=6)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.name