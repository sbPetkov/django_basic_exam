from django.db import models
from django import forms

from world_of_speed.custom_validators.profile_validators import custom_min_length_validator, validate_user, validate_age


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MAX_PASSWORD_LENGTH = 20
    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25

    username = models.CharField(max_length=MAX_USERNAME_LENGTH,
                                validators=[custom_min_length_validator,
                                            validate_user],
                                blank=False,
                                null=False,
                                )

    email = models.EmailField(blank=False, null=False)

    age = models.SmallIntegerField(blank=False,
                                   null=False,
                                   validators=[validate_age],
                                   )

    password = models.CharField(max_length=MAX_PASSWORD_LENGTH,
                                blank=False,
                                null=False,
                                )

    first_name = models.CharField(max_length=MAX_FIRST_NAME_LENGTH,
                                  blank=True,
                                  null=True,
                                  )

    last_name = models.CharField(max_length=MAX_LAST_NAME_LENGTH,
                                 blank=True,
                                 null=True,
                                 )

    profile_picture = models.URLField(blank=True, null=True)