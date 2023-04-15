from django.contrib import admin
from .models import Character, Attribute, CharAttribute



class CharAttributeInline(admin.TabularInline):
    model = CharAttribute
    extra = 0
    def has_add_permission(self, request, obj):
        return False


class CharacterAdmin(admin.ModelAdmin):
    
    fieldsets =[
        (None, {"fields": [("name", "level", "current_exp"), ("current_health", "current_corruption")]})
    ]
    inlines = [ CharAttributeInline,]
    
   


# Register your models here.
admin.site.register(Character, CharacterAdmin)
admin.site.register(Attribute)

