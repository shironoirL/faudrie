from django.shortcuts import render, get_object_or_404
from .models import DrugInformation
from django.views.generic import ListView
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
    return render(request,
                  'audrie/druginfo/detail.html',
                  {'drug': drug})

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



# class mechanismOfActionListView(ListView):
#     queryset = MechanismOfAction.objects.all()
#     context_object_name = 'mechanisms'
#     template_name = 'audrie/druginfo/list.html'
