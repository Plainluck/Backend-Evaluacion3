from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Element(models.Model):
    name = models.CharField(max_length = 20)
    effectiveness = models.CharField(max_length=12)
    weakness = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Expansion(models.Model):
    name = models.CharField(max_length = 30)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length = 20)
    skill = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Card(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=False)
    element = models.ManyToManyField(to='Element', related_name='card_elements')
    expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE, null=False)
    HP = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(340)])

    def __str__(self):
        return str(self.pokemon)
    