from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class ActiveSkill(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    default_value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], 
                                      default=1)
    

class Attribute(models.Model):
    name = models.IntegerField(validators=[MinValueValidator(1)], default=10)

class Character(models.Model):
    name = models.CharField(max_length=255, blank=True)
    level = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    current_exp = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    current_health = models.IntegerField(default=30)
    current_corruption = models.IntegerField(default=10)        

class Attributes(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key=True)
    strength = models.IntegerField(validators=[MinValueValidator(1)], default=10)
    dexterity = models.IntegerField(validators=[MinValueValidator(1)], default=10)
    constitution = models.IntegerField(validators=[MinValueValidator(1)], default=10)
    wisdom = models.IntegerField(validators=[MinValueValidator(1)], default=10)
    intelligence = models.IntegerField(validators=[MinValueValidator(1)], default=10)
    charisma = models.IntegerField(validators=[MinValueValidator(1)], default=10)

