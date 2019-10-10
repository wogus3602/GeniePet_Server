from django.db import models
import numpy as np
# Create your models here.
class Feed(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    image = models.URLField()
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name


class Dog(models.Model):
    #user foreignKey
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    species = models.CharField(max_length=50)
    def __str__(self):
        return self.name+': '+self.species
 
class Review(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    feed = models.ForeignKey(Feed,on_delete=models.CASCADE, related_name="review")
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)