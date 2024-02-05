from django.urls import path
from . import views

app_name = 'druginfo'

urlpatterns = [
    # post views
    path('', views.drug_list, name='drug_list'),
    path('<int:id>/', views.drug_detail, name='drug_detail'),
]
