from django.shortcuts import render



# Create your views here.
rooms = [
    {'id': 2, 'name': 'Lets learn python'},
    {'id': 3, 'name': 'Frontend development'},
    {'id': 4, 'name': 'Backend development'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')