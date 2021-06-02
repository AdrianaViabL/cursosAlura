from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consulta', views.review_consulta, name='review_consulta')
]

