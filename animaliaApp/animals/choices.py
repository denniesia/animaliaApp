from django.db import models


class OwnerGenderChoice(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    UNKNOWN = 'U', 'Unknown'