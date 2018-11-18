from django.shortcuts import render, redirect
from collection.forms import RocketForm
from collection.models import Rocket
from django.template.defaultfilters import slugify

def index(request):
    rockets = Rocket.objects.all()
    return render(request, 'index.html', {
        'rockets': rockets,
    })

def rocket_detail(request, slug):
    rocket = Rocket.objects.get(slug=slug)
    return render(request, 'rockets/rocket_detail.html', {
        'rocket': rocket,
    })

def edit_rocket(request, slug):
    rocket = Rocket.objects.get(slug=slug)
    form_class = RocketForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=rocket)
        if form.is_valid():
            form.save()
            return redirect('rocket_detail', slug=rocket.slug)
    else:
        form = form_class(instance=rocket)
    return render(request, 'rockets/edit_rocket.html', {
        'rocket': rocket,
        'form': form,
    })

def create_rocket(request):
    form_class = RocketForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            rocket = form.save(commit=False)
            rocket.user = request.user
            rocket.slug = slugify(rocket.name)
            rocket.save
            return redirect('rocket_detail', slug=rocket.slug)
    else:
        form = form_class()
    return render(request, 'rockets/create_rocket.html', {
        'form': form,
    })