from django.shortcuts import render, get_object_or_404
from .models import DrugInformation


def drug_list(request):
    drugs = DrugInformation.published.all()
    return render(request,
                 'audrie/druginfo/list.html',
                 {'drugs': drugs})


def drug_detail(request, id):
    drug = get_object_or_404(DrugInformation,
                             id=id,
                             status=DrugInformation.Status.PUBLISHED)
    return render(request,
                  'audrie/druginfo/detail.html',
                  {'drug': drug})