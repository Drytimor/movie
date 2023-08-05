from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)
    slug = models.SlugField(default='', null=False, db_index=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



    def get_url(self):
        return reverse('details-movie', args=[self.slug])


    def __str__(self):
        return f'{self.name} - {self.rating}'


