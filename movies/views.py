from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm
from .models import Movies
# Create your views here.


def create_movie(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movies-list')
    return render(request, 'movie_detail.html', {'movie_form_add': form})


def update_movie(request, id):
    instance = get_object_or_404(Movies, id=id)
    form = MovieForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('movies-list')
    return render(request, 'movie_detail.html', {'movie_form': form})


def delete_movie(request, id):
    instance = get_object_or_404(Movies, id=id)
    instance.delete()
    return redirect('movies-list')
