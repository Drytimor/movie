from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class DressingRoom(models.Model):
    floor = models.IntegerField(validators=(MinValueValidator(0), MaxValueValidator(100)))
    number = models.IntegerField(validators=(MinValueValidator(0), MaxValueValidator(1000)))

    def __str__(self):
        return f'{self.floor} {self.number}'


class Actor(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER, default=MALE)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)

    def get_url(self):
        return reverse('details-actor', args=[self.id])

    def __str__(self):
        if self.gender == self.MALE:
            return f"Актер {self.first_name} {self.last_name}"
        return f"Актриса {self.first_name} {self.last_name}"


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def get_url(self):
        return reverse('details-director', args=[self.id])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Movie(models.Model):

    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    budget = models.IntegerField(default=1000000, blank=True, validators=[MinValueValidator(1)])
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='actors')
    slug = models.SlugField(default=slugify(name), null=False, db_index=True)


    def get_url(self):
        return reverse('details-movie', args=[self.slug])


    def __str__(self):
        return f'{self.name} - {self.rating}'


