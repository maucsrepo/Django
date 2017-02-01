from django.shortcuts import render
from Tennis.helpers import extractor


def homepage(request):
    list_in = {"Nombre":'Valor'}
    data = extractor.extract_sets(list_in)
    return render(request, 'Tennis/homepage.html', {'data': data})


def index(request):
    return render(request, 'Tennis/index.html')


def players(request):
    return render(request, 'Tennis/players.html')


def player_profile(request, player_id):
    return render(request, 'Tennis/player_detail.html', {'player_id': player_id})

