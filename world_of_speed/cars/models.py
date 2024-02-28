from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from world_of_speed.custom_validators.car_validators import year_validator
from world_of_speed.profiles.models import Profile


class Car(models.Model):
    MAX_TYPE_LENGTH = 10
    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1
    MIN_PRICE = 1

    TYPE_CHOICES = [
        ("Rally", "Rally"),
        ("Open-wheel", "Open-wheel"),
        ("Kart", "Kart"),
        ("Drag", "Drag"),
        ("Other", "Other"),
    ]

    type = models.CharField(max_length=MAX_TYPE_LENGTH,
                            blank=False,
                            null=False,
                            choices=TYPE_CHOICES,
                            )

    model = models.CharField(max_length=MAX_MODEL_LENGTH,
                             validators=[MinLengthValidator(MIN_MODEL_LENGTH)],
                             blank=False,
                             null=False,
                             )

    year = models.IntegerField(validators=[year_validator],
                               blank=False,
                               null=False,
                               )

    image = models.URLField(blank=False,
                            null=False,
                            unique=True,
                            error_messages={'unique': "This image URL is already in use! Provide a new one."},
                            )

    price = models.FloatField(blank=False,
                              null=False,
                              validators=[MinValueValidator(MIN_PRICE)],
                              )

    owner = models.ForeignKey(Profile,
                              on_delete=models.CASCADE,
                              blank=False,
                              null=False,
                              )