from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.URLField(max_length=200)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)