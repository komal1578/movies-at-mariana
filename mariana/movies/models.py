from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='images/')
    genres = models.ManyToManyField('Genre')
    rating = models.CharField(max_length=10)
    year_release = models.DateField()
    metacritic_rating = models.IntegerField()
    runtime = models.IntegerField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name