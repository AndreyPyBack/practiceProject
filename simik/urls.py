from django.urls import path

from practiceProject.simik import views

urlpatterns = [
    path('', views.index, name='broSimik'),
]

# Жёсткая жопа
