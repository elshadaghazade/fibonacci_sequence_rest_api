from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('<end_idx>/', calc_fibonacci_sequence),
    path('<start_idx>/<end_idx>/', calc_fibonacci_sequence)
]
