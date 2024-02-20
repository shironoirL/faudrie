from django.contrib import admin
from .models import DrugInformation,MechanismOfAction, useIndication, pathContribution, metapathContribution, sourceEdgeContribution, targetEdge

@admin.register(DrugInformation)
class PostAdmin(admin.ModelAdmin):
    list_display = ['drugbankID', 'drugname', 'description', 'moleculeType']

@admin.register(MechanismOfAction)
class PostAdmin(admin.ModelAdmin):
    list_display = ['mechanism','targetReceptor', 'humanReceptor', 'links']

@admin.register(useIndication)
class PostAdmin(admin.ModelAdmin):
    list_display = ['indicationInfo', 'therapeuticInfo', 'phase', 'references']

@admin.register(pathContribution)
class PostAdmin(admin.ModelAdmin):
    list_display = ['verbosePath', 'percentOfPrediction']

@admin.register(metapathContribution)
class PostAdmin(admin.ModelAdmin):
    list_display = ['verbose', 'percentOfPrediction']

@admin.register(sourceEdgeContribution)
class PostAdmin(admin.ModelAdmin):
    list_display = ['sourceEdge', 'percentOfPrediction']

@admin.register(targetEdge)
class PostAdmin(admin.ModelAdmin):
    list_display = ['targetEdge', 'percentOfPrediction']