from django.shortcuts import render, get_object_or_404
from .models import DrugInformation, MechanismOfAction, useIndication
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from django.contrib.postgres.search import TrigramSimilarity

def drug_list(request):
    drugs = DrugInformation.published.all()
    return render(request,
                  'audrie/druginfo/list.html',
                  {'drugs': drugs})


def drug_detail(request, id):
    drug = get_object_or_404(DrugInformation,
                             id=id,
                             status=DrugInformation.Status.PUBLISHED)
    mechanism_of_action = drug.mechanismofaction_set.all()
    indications = drug.useindication_set.all()
    pathContributions = drug.pathcontribution_set.all()
    metapathContributions = drug.metapathcontribution_set.all()
    sourceEdgeContributions = drug.sourceedgecontribution_set.all()
    targetEdges = drug.targetedge_set.all()
    return render(request,
                  'audrie/druginfo/detail.html',
                  {'drug': drug, 'mechanisms': mechanism_of_action, 'indications': indications, 'pathContributions': pathContributions,
                   'metapathContributions': metapathContributions, 'sourceEdgeContributions': sourceEdgeContributions, 'targetEdges': targetEdges})


class DrugListView(ListView):
    queryset = DrugInformation.published.all()
    context_object_name = 'drugs'
    template_name = 'audrie/druginfo/list.html'

def drug_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = DrugInformation.published.annotate(
                similarity=TrigramSimilarity('drugname', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')

    return render(request,
                  'audrie/druginfo/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
