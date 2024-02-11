from django.contrib import admin
from .models import DrugInformation,MechanismOfAction

@admin.register(DrugInformation)
class PostAdmin(admin.ModelAdmin):
    list_display = ['drugbankID', 'drugname', 'description', 'moleculeType']

@admin.register(MechanismOfAction)
class PostAdmin(admin.ModelAdmin):
    list_display = ['mechanism','targetReceptor', 'humanReceptor', 'links']
