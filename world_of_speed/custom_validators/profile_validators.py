from django.core.exceptions import ValidationError


def custom_min_length_validator(username):
    is_valid = True if len(username) > 2 else False

    if not is_valid:
        raise ValidationError("Username must be at least 3 chars long!")


def validate_user(username):
    is_valid = all(ch.isalnum() or ch == "_" for ch in username)

    if not is_valid:
        raise ValidationError("Username must contain only letters, digits, and underscores!")


def validate_age(age):
    is_valid = (age >= 21)

    if not is_valid:
        raise ValidationError("Age requirement: 21 years and above.")