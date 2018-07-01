from django.contrib import admin
from . import models

class CycleAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'cycle_reward', 'cycle_limit')
admin.site.register(models.CycleModel, CycleAdmin)

class AccumulationAdmin(admin.ModelAdmin):
    list_display = ('username', 'created_at', 'production_id', 'production_number', 'coefficient', 'accumulation_number', 'comment', 'cycle_id', 'cycle_reward')
admin.site.register(models.Accumulation, AccumulationAdmin)