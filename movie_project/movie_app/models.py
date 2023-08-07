from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator



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
    slug = models.SlugField(default='', null=False, db_index=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



    def get_url(self):
        return reverse('details-movie', args=[self.slug])


    def __str__(self):
        return f'{self.name} - {self.rating}'


