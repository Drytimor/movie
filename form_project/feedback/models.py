from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(1)])
    surname = models.CharField(max_length=40, validators=[MinLengthValidator(1)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])