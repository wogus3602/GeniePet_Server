from django.db import models

# Create your models here.
class feed(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=15)
    create_date = models.DateTimeField(auto_created=True, auto_now_add=True)