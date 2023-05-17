from django.db import models
from django.contrib import admin
from . models import ChaosFactor, Probability, FateChart, Game, Scene, RandomEventFocus, MeaningTable, MeaningTableElement, SceneAdjustmentOption, List, SceneMessage, Note

# Register your models here.
class ChaosFactorAdmin(admin.ModelAdmin):
    readonly_fields = ['intencity'] # Add any other fields you want to display here

    def get_readonly_fields(self, request, obj=None):     
        if obj:
            return self.readonly_fields 
        return self.readonly_fields

class FateChartInline(admin.TabularInline):
    model = FateChart   
    def has_add_permission(self, request, obj):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

class MeaningTableElementInline(admin.TabularInline):
    model = MeaningTableElement
    extra = 0

class ProbabilityAdmin(admin.ModelAdmin):
    inlines = [ FateChartInline]

class MeaningTableAdmin(admin.ModelAdmin):
    inlines = [MeaningTableElementInline]
 

#admin.site.register(ChaosFactor, ChaosFactorAdmin)
admin.site.register(Probability, ProbabilityAdmin)
admin.site.register(Game)
admin.site.register(Scene)
admin.site.register(RandomEventFocus)
#admin.site.register(MeaningTableElement)
admin.site.register(MeaningTable, MeaningTableAdmin)
admin.site.register(SceneAdjustmentOption)
admin.site.register(List)
admin.site.register(SceneMessage)
admin.site.register(Note)
#admin.site.register(FateChart)



