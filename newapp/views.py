from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.

def movie_list(request):
    movies_objects = Movies.objects.all()

    movie_name = request.GET.get('mvoie_name')
    
    if movie_name != '' and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains=movie_name)

    paginator = Paginator(movies_objects, 4)
    page = request.GET.get('page')
    movies_objects = paginator.get_page(page)

    return render(request, 'newapp/movie_list.html', {'movie_objects':movies_objects})