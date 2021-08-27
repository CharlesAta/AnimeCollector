from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

RECOMMENDATIONS = (
    ('Y', 'Yes'),
    ('M', 'Maybe'),
    ('N', 'No')
)
class Merch(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('merch_detail', kwargs={'pk': self.id})
        
# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    description = models.TextField(max_length=400)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    merch = models.ManyToManyField(Merch)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={"anime_id": self.id})

class Review(models.Model):
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    recommend = models.CharField(
        max_length=1,
        choices=RECOMMENDATIONS,
        default=RECOMMENDATIONS[1][0]
        )
    comment = models.TextField(max_length=200)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_recommend_display()} on {self.date}"

    class Meta:
        ordering = ['-date']