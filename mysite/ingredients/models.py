from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='ingredients')

    def str(self):
        return self.name
