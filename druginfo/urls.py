from django.urls import path
from . import views

app_name = 'druginfo'

urlpatterns = [
    # post views
    path('', views.DrugListView.as_view(), name='drug_list'),
    path('<int:id>/', views.drug_detail, name='drug_detail'),
    path('search/', views.drug_search, name='drug_search'),
]
