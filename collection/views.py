from django.shortcuts import render

# Create your views here.
def index(request):
    number = 5
    return render(request, 'index.html', {
        'number': number,
    })