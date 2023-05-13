from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

MEANING_TABLE_TYPES = [
        ("ACTION", "Action"),
        ("DESCRIPTION", "Description"),
        ("ELEMENT", "Element"),
    ]

LIST_TYPES = [
    ('CHARACTER', "Character"),
    ('THREAD', "Thread")
]
class ChaosFactor(models.Model):
    intencity = models.BigAutoField(validators=[MinValueValidator(1), MaxValueValidator(9)], primary_key=True)
    def __str__(self):
        return str(self.intencity)

class Probability(models.Model):
    #not a primary key because we do a bunch of staff on save if the new probability doesn't have a primary key.
    #if description is pk, it never happens.
    description = models.CharField(max_length=255, unique=True)

    probability_to_chaos_factor = models.ManyToManyField(ChaosFactor, through="FateChart")

    def __str__(self):
        return self.description
    
    def save(self, *args, **kwargs):        
        if not self.pk: 
            super().save(*args, **kwargs)  
            chaos_factors = ChaosFactor.objects.all()
            self.probability_to_chaos_factor.add(*chaos_factors)
        else:
            super().save(*args, **kwargs)  

class FateChart(models.Model):
    probability = models.ForeignKey(Probability, on_delete=models.PROTECT)
    chaos_factor = models.ForeignKey(ChaosFactor, on_delete=models.PROTECT)
    exceptional_yes_if_equal_or_lower = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    yes_if_equal_or_lower = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    exceptional_no_if_equal_or_higher = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return str(self.probability) + "CF: " + str(self.chaos_factor)
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['probability', 'chaos_factor'], name='unique_chaos_factor_probability')
        ]


class RandomEventFocus(models.Model):
    yes_if_equal_or_lower = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=1)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class MeaningTable(models.Model):
    type = models.CharField(max_length=155, choices=MEANING_TABLE_TYPES)
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.type + ": " + self.name

class MeaningTableElement(models.Model):
    table = models.ForeignKey(MeaningTable, on_delete=models.PROTECT)
    word = models.CharField(max_length=100)
    
    def __str__(self):
        return self.table.name + ": " + self.word 

    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['table', 'word'], name='unique_word_in_table')
        ]

class SceneAdjustmentOption(models.Model):
    yes_if_equal_or_lower =models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1, unique=True)
    name = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return str(self.yes_if_equal_or_lower) + ": " + self.name



class Game(models.Model):
   
   

    name = models.CharField(max_length=255)
    current_chaos_factor = models.ForeignKey(ChaosFactor, on_delete=models.PROTECT, default =5)
    active_scene = models.ForeignKey('Scene', on_delete=models.PROTECT,related_name='games', null = True, blank=True)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):        
        if not self.pk:             
            super().save(*args, **kwargs) 
            new_character_list = List(type = "CHARACTER", game = self)
            new_thread_list = List(type = "THREAD", game = self)
            new_character_list.save()
            new_thread_list.save()
        else:
            super().save(*args, **kwargs)  

class List(models.Model):
    type = models.CharField(max_length=155, choices=LIST_TYPES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.name + ": " + self.type + " list"

    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['type', 'game'], name='unique_list_in_game')
        ]

class ListNote(models.Model):
    note_list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.TextField(blank = True, null=True)

class Scene(models.Model):
    name = models.CharField(max_length=255, default= "Scene")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.game) + ": " + self.name

    def save(self, *args, **kwargs):        
        if not self.pk and self.name == Scene._meta.get_field('name').default:              
            number_of_scenes = Scene.objects.filter(game = self.game.id).count()
            self.name = Scene._meta.get_field('name').default + " " + str(number_of_scenes+1)
            super().save(*args, **kwargs) 
        else:
            super().save(*args, **kwargs)  
