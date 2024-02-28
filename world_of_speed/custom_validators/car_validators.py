from django.core.exceptions import ValidationError


def year_validator(year):
    if 1999 <= year <= 2030:
        is_valid = True
    else:
        is_valid = False

    if not is_valid:
        raise ValidationError("Year must be between 1999 and 2030!")