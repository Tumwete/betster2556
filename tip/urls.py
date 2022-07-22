from django.urls import path
from . import views



urlpatterns = [
    path('', views.tip, name="tip"),
    path('multi/', views.multiple, name="multiple"),
    
]
