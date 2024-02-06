from django.db import models
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                        .filter(status=DrugInformation.Status.PUBLISHED)

class DrugInformation(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', "Draft"
        PUBLISHED = 'PB', "Published"

    drugbankID = models.CharField(max_length=250)
    drugname = models.CharField(max_length=250)
    description = models.TextField(max_length=2500)
    moleculeType = models.CharField(max_length=250)
    yearOfDrug = models.PositiveIntegerField()
    confirmStatus = models.CharField(max_length=250)
    drugFamily = models.CharField(max_length=250)
    synonyms = models.CharField(max_length=250)
    smiles = models.CharField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()


    def __str__(self):
        return self.drugname
    def get_absolute_url(self):
        return reverse('druginfo:drug_detail',
                       args=[self.id])





# Create your models here.
