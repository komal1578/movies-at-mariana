from django.shortcuts import render
from .models import Movie, Genre

def home(request):
    return render(request,"home.html")

def index(request):
    search_query = request.GET.get('search_query', '')
    selected_genres = request.GET.getlist('genre')
    
    movies = Movie.objects.all()
    
    if search_query:
        movies = movies.filter(title__icontains=search_query)
    
    if selected_genres:
        movies = movies.filter(genres__name__in=selected_genres).distinct()
    
    movies = movies.order_by('-year_release')
    
    genres = Genre.objects.all()
    context = {"movies": movies, "genres": genres, "search_query": search_query, "selected_genres": selected_genres}
    return render(request, "index.html", context=context)