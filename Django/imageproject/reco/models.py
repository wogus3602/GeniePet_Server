from django.db import models

# Create your models here.
class feed(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=15)
    rating = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        ordering = ['-rating', ]


class Dog(models.Model):
    #user foreignKey
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    species = models.CharField(max_length=50)
    def __str__(self):
        return self.name+': '+self.species
 
class Rank(models.Model):

    class Meta(object):
        unique_together = (("date", "dog"), )

    date = models.DateField(db_index=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    value = models.IntegerField()