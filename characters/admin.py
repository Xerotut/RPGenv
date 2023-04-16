from django.contrib import admin
from .models import Character, Attribute, CharAttribute, Skill, CharSkill, Flaw, FlawDescription



class CharAttributeInline(admin.TabularInline):
    model = CharAttribute
    extra = 0
    def has_add_permission(self, request, obj):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
   

class CharSkillInline(admin.TabularInline):
    model = CharSkill
    extra = 0


    

class CharacterAdmin(admin.ModelAdmin):
    
    fieldsets =[
        (None, {"fields": [("name", "level", "current_exp"), ("current_health", "current_corruption")]}),
        (None, {"fields": [("flaw")]})
    ]
    inlines = [ CharAttributeInline, CharSkillInline]
    
   
class FlawDescriptionInline(admin.StackedInline):
    model = FlawDescription   
    def has_add_permission(self, request, obj):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

class FlawAdmin(admin.ModelAdmin):
    inlines = [FlawDescriptionInline]

# Register your models here.
admin.site.register(Character, CharacterAdmin)
admin.site.register(Attribute)
admin.site.register(Skill)
admin.site.register(CharSkill)
admin.site.register(Flaw, FlawAdmin)



