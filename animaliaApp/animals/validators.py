from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class NoSpecialSignsValidator:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        special_signs = ['%', '§', '/', '?', '#', '*']

        if any(char in special_signs for char in value.strip()):
            raise ValidationError(self.message)

@deconstructible
class OnlyLettersValidator:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        if not all(c.isalpha() or c.isspace() for c in value.strip()):
            raise ValidationError(self.message)