from django.urls import path
from . import views

urlpatterns = [
    path('compass/', views.index, name='index'),
    path('instructions/<int:instruction_id>/', views.instruction_detail, name='instruction_detail'),
]