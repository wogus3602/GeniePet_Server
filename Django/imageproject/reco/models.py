from django.db import models

# Create your models here.
class feed(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=15)
    rating = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        ordering = ['-rating', ]