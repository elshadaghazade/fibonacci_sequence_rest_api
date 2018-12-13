from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(31536000)
def home(request):
    return render(request, 'home/home.html')