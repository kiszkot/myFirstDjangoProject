from django.db import models

# Create your models here.

RECIPE_TYPES = [
    ('M', 'Meat'),
    ('Ve', 'Vegan'),
    ('V', 'Vegetarian'),
]

class CEO(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Chef(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=60)
    recipe_type = models.CharField(
        choices=RECIPE_TYPES, max_length=12)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

    class Meta:
        ordering = ["recipe_name"]

    def __str__(self):
        return "%s (%s), by %s" % (self.recipe_name, self.recipe_type, self.chef)


class Restaurant(models.Model):
    business_name = models.CharField(max_length=60)
    recipes = models.ManyToManyField(Recipe)
    headmaster = models.ForeignKey(CEO, on_delete=models.CASCADE)

    class Meta:
        ordering = ['business_name']

    def __str__(self):
        return self.business_name 
