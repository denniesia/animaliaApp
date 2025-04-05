from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from .validators import NoSpecialSignsValidator, OnlyLettersValidator
from .choices import OwnerGenderChoice
from .mixins import CreatedAt
from datetime import date
# Create your models here.
class Category(CreatedAt):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.name

class Owner(CreatedAt):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(1),
            OnlyLettersValidator('Owner names must contain only letters'),
        ]
    )
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=OwnerGenderChoice,
    )
    image_url = models.URLField(null=True, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    hobby = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

class Animal(CreatedAt):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            NoSpecialSignsValidator('Animal names cannot contain special characters - %, §, /, ?, #, *.')
        ]
    )
    birthdate = models.DateField()
    age = models.IntegerField()
    image_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    fav_food = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL,related_name= 'animals', null=True, blank=True)


    def __str__(self):
        return self.name


class Rating(CreatedAt):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ]
    )

    def __str__(self):
        return self.value
