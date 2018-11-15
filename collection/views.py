from django.shortcuts import render
from collection.models import Rocket
# Create your views here.
def index(request):
    rockets = Rocket.objects.all()
    return render(request, 'index.html', {
        'rockets': rockets,
    })