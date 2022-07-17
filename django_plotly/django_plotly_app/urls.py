from django.urls import path
from . import views

urlpatterns = [
    path('demo-plot/', views.demo_plot_view),
    path('index/', views.index)
]