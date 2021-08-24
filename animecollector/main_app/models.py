from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    description = models.TextField(max_length=400)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"anime_id": self.id})