from django.db import models, IntegrityError
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.





class Attribute(models.Model):
    name = models.CharField(max_length=100, blank=True, unique= True)
    abbreviation = models.CharField(max_length=3, blank=True)
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
 

class Skill(models.Model):
    DEFAULT_TYPES =[
        ("INT","Value"),
        ("ATR","Attribute"),
        ("ATR+ATR","Sum of attributes"),
    ]
    SKILL_TYPES = [
        ("BS", "Basic"),
        ("ADV", "Advanced"),
    ]
    name = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=3, choices = SKILL_TYPES, default="BS")
    default_type = models.CharField(max_length=10, choices= DEFAULT_TYPES, default="INT")
    default_value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], 
                                      default=0)
    default_attribute = models.ForeignKey(Attribute, null=True, on_delete=models.SET_NULL, blank=True)
    default_attribute_comb = models.ManyToManyField(Attribute, related_name="skill_default_attribute_comb", blank=True)
       
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.type == "BS":            
            super().save(*args, **kwargs)
            characters = Character.objects.all()
            for character in characters:
                try:
                    character.skills.add(self)       
                except IntegrityError:
                        pass
        else:
            super().save(*args, **kwargs)     
    
class Flaw(models.Model):    
 
    name = models.CharField(max_length=255, default= "New flaw", unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): 
        if not self.pk:             
            super().save(*args, **kwargs)   
            for level in FlawDescription.INTENSITY_LEVELS:                 
                new_flaw_description = FlawDescription(flaw = self, intensity = level[0])
                new_flaw_description.save()
        else:
            super().save(*args, **kwargs)           

class FlawDescription(models.Model):
    INTENSITY_LEVELS = [
        ("FIRST", "I"),
        ("SECOND", "II"),
        ("THIRD", "III"),
    ]
    flaw = models.ForeignKey(Flaw, on_delete=models.CASCADE)
    intensity = models.CharField(max_length=6, choices=INTENSITY_LEVELS, default="I")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.flaw.name + " " + self.intensity
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['flaw', 'intensity'], name='unique_flaw_intensity')
        ]
    
class Advantage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Character(models.Model):
    name = models.CharField(max_length=255, default= "New character")
    level = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    current_exp = models.IntegerField("Current experience",validators=[MinValueValidator(0)], default=0)
    current_health = models.IntegerField(default=30)
    current_corruption = models.IntegerField(default=10)
    attributes = models.ManyToManyField(Attribute, through="CharAttribute")        
    skills = models.ManyToManyField(Skill, through="CharSkill")        
    flaw = models.ForeignKey(Flaw,null=True, blank=True, on_delete=models.SET_NULL)
    advantage = models.ForeignKey(Advantage,null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        
        if not self.pk:   
            super().save(*args, **kwargs)         
            attributes = Attribute.objects.all()
            self.attributes.add(*attributes)  
            skills = [skill for skill in Skill.objects.all() if skill.type=="BS"] 
            self.skills.add(*skills)          
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
    
    

class CharSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    allocated_points = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], 
                                      default=0)
    
    def __str__(self):
        return self.character.name +" " + self.skill.name
   
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['character', 'skill'], name='unique_skill')
        ]
