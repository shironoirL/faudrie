from django.db import models
from django.utils import timezone
from django.urls import reverse
from rdkit import Chem
from rdkit.Chem import Draw
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    chemBLReference = models.CharField(max_length=250, default='somereference')
    drugbankReference = models.CharField(max_length=250, default='somereference')
    dailymedReference = models.CharField(max_length=250, default='somereference')
    smiles_image = models.ImageField(upload_to='smilesimages/', blank=True, null=True)

    def __str__(self):
        return self.drugname
    def get_absolute_url(self):
        return reverse('druginfo:drug_detail',
                       args=[self.id])
class MechanismOfAction(models.Model):
    mechanism = models.CharField(max_length=250)
    targetReceptor = models.CharField(max_length=250)
    humanReceptor = models.CharField(max_length=250)
    links = models.CharField(max_length=250)
    drugbankID = models.ManyToManyField(DrugInformation)
    def __str__(self):
        return self.mechanism
    def get_absolute_url(self):
        return reverse('druginfo:drug_detail',
                       args=[self.id])

    @receiver(pre_save, sender=DrugInformation)
    def generate_smiles_image(sender, instance, **kwargs):
        if instance.smiles:
            mol = Chem.MolFromSmiles(instance.smiles)
            if mol is not None:
                img = Draw.MolToImage(mol, size=(300, 300))
                img_path = f'media/smilesimages/{instance.smiles[:20]}.png'
                img.save(img_path)
                instance.smiles_image = img_path

class useIndication(models.Model):
    indicationInfo = models.CharField(max_length=250)
    therapeuticInfo = models.CharField(max_length=250)
    phase = models.PositiveIntegerField()
    references = models.CharField(max_length=250)
    drugbankID = models.ManyToManyField(DrugInformation)
    def __str__(self):
        return self.indicationInfo
    def get_absolute_url(self):
        return reverse('druginfo:drug_detail',
                       args=[self.id])






# Create your models here.
