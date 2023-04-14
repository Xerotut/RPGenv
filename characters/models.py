from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class ActiveSkill(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    default_value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], 
                                      default=1)
    

class Attribute(models.Model):
    name = models.CharField(max_length=100, blank=True)

class Character(models.Model):
    name = models.CharField(max_length=255, blank=True)
    level = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    current_exp = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    current_health = models.IntegerField(default=30)
    current_corruption = models.IntegerField(default=10)
    attributes = models.ManyToManyField(Attribute, through="CharAttributes")        

class CharAttributes(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, primary_key=True)
    value = models.IntegerField(alidators=[MinValueValidator(1)], default=10)
    

class CharActiveSkill(models.Model):
    character = models.models.ForeignKey(Character, on_delete=models.CASCADE, primary_key=True)
    active_skill = models.models.ForeignKey(ActiveSkill, on_delete=models.CASCADE, primary_key=True)