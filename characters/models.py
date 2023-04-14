from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class ActiveSkill(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    default_value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], 
                                      default=0)
    

class Attribute(models.Model):
    name = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.pk:           
            characters = Character.objects.all()
            for character in characters:
                character.attributes.add(self)
    

class Character(models.Model):
    name = models.CharField(max_length=255, blank=True)
    level = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    current_exp = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    current_health = models.IntegerField(default=30)
    current_corruption = models.IntegerField(default=10)
    attributes = models.ManyToManyField(Attribute, through="CharAttributes")        

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.pk:
            attributes = Attribute.objects.all()
            self.attributes.add(*attributes) 
    

class CharAttribute(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, primary_key=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, primary_key=True)
    value = models.IntegerField(alidators=[MinValueValidator(1)], default=10)

    def __str__(self):
        return self.character + self.attribute
    
    

class CharActiveSkill(models.Model):
    character = models.models.ForeignKey(Character, on_delete=models.CASCADE, primary_key=True)
    active_skill = models.models.ForeignKey(ActiveSkill, on_delete=models.CASCADE, primary_key=True)
    allocated_points = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], 
                                      default=0)
    
    def __str__(self):
        return self.character + self.active_skill