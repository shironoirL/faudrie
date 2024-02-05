from django.contrib import admin
from .models import DrugInformation

@admin.register(DrugInformation)
class PostAdmin(admin.ModelAdmin):
    list_display = ['drugbankID', 'drugname', 'description', 'moleculeType']

# Register your models here.
