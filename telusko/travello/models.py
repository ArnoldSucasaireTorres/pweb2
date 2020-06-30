from django.db import models

# Create your models here.

class Destination(models.Model):

    name : str
    img : str
    desc : str
    price: int
    offer : bool

