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
        
        if not self.pk:  
            super().save(*args, **kwargs)         
            characters = Character.objects.all()
            for character in characters:
                character.attributes.add(self)
        else:
            super().save(*args, **kwargs)
    

class Character(models.Model):
    name = models.CharField(max_length=255, default= "New character")
    level = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    current_exp = models.IntegerField("Current experience",validators=[MinValueValidator(0)], default=0)
    current_health = models.IntegerField(default=30)
    current_corruption = models.IntegerField(default=10)
    attributes = models.ManyToManyField(Attribute, through="CharAttribute")        

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        
        if not self.pk:   
            super().save(*args, **kwargs)         
            attributes = Attribute.objects.all()
            self.attributes.add(*attributes)             
        else: 
            super().save(*args, **kwargs)
    

class CharAttribute(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(1)], default=10)

    def __str__(self):
        return self.character.name + " " + self.attribute.name
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['character', 'attribute'], name='unique_attribute')
        ]
    
    

class CharActiveSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    active_skill = models.ForeignKey(ActiveSkill, on_delete=models.CASCADE)
    allocated_points = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], 
                                      default=0)
    
    def __str__(self):
        return self.character + self.active_skill
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['character', 'active_skill'], name='unique_active_skill')
        ]
