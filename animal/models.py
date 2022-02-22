from django.db import models


class Animal(models.Model):
    ANIMAL_TYPE = [
        ("h", "Хищник"),
        ("t", "Травоядный"),
    ]

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    types = models.CharField(max_length=50, choices=ANIMAL_TYPE,blank=True, null=True)



