from django.db import models

# Create your models here.
class feed(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    


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