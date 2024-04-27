from django.urls import path
from .views import CovidDataAPIView

urlpatterns = [
    path('covid-data/', CovidDataAPIView.as_view(), name='covid_data_list_create'),
    path('covid-data/<int:id>/', CovidDataAPIView.as_view(), name='covid_data_rud'),
    path('covid-data/filter/<str:key_column>/<str:key_value>/', CovidDataAPIView.as_view(), name='covid_data_filter'),
]


