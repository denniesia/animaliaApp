from django.shortcuts import render, redirect, get_object_or_404
from animaliaApp.animals.models import Animal, Owner, Category
from animaliaApp.animals.forms import CategoryForm, AnimalAddForm, OwnerAddForm, DeleteAnimalForm, EditAnimalForm, \
    OwnerEditForm, OwnerDeleteForm, RatingForm
from django.db.models import Avg, Count

# Create your views here.
def index_view(request):
    return render(request, 'common/index.html')

def dashboard_view(request):
    animals = Animal.objects.annotate(avg_rating=Avg('ratings__value'))
    owners = Owner.objects.all()
    context = {'animals': animals, 'owners': owners}
    return render(request, 'common/dashboard.html', context)

def create_animal_view(request):
    if request.method == 'GET':
        form = AnimalAddForm()
    else:
        form = AnimalAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}

    return render(request, 'animals/create-animal.html', context)

def create_owner_view(request):
    if request.method == 'GET':
        form = OwnerAddForm()
    else:
        form = OwnerAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}

    return render(request, 'owners/create-owner.html', context)
def delete_animal_view(request, pk):
    animal = Animal.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteAnimalForm(instance=animal)
    else:
        form = DeleteAnimalForm(request.POST, instance=animal)
        if form.is_valid():
            animal.delete()
            return redirect('index')
    context = {'form': form, 'animal': animal}
    return render(request, 'animals/delete-animal.html', context)

def details_animal_view(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    avg_rating = animal.ratings.aggregate(avg_rating=Avg('value'))['avg_rating']

    if avg_rating is None:
        avg_rating = 'No ratings yet'

    context = {
        'animal': animal,
        'avg_rating': avg_rating,
    }

    return render(request, 'animals/details-animal.html', context)
def edit_animal_view(request, pk):
    animal = Animal.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditAnimalForm(instance=animal)
    else:
        form = EditAnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'animal': animal}
    return render(request, 'animals/edit-animal.html', context)

def create_category_view(request):
    if request.method == "GET":
        form = CategoryForm()
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'categories/create-category.html', context)

def edit_owner_view(request, pk):
    owner = Owner.objects.get(pk=pk)
    if request.method == "GET":
        form = OwnerEditForm(instance=owner)
    else:
        form = OwnerEditForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'owner': owner}

    return render(request, 'owners/edit-owner.html', context)

def delete_owner_view(request, pk):
    owner = Owner.objects.get(pk=pk)
    if request.method == 'GET':
        form = OwnerDeleteForm(instance=owner)
    else:
        form = OwnerDeleteForm(request.POST, instance=owner)
        if form.is_valid():
            owner.delete()
            return redirect('index')
    context = {'form': form, 'owner': owner}
    return render(request, 'owners/delete-owner.html', context)

def details_owner_view(request, pk):
    owner = Owner.objects.annotate(animals_count=Count('animals')).get(pk=pk)
    animals = owner.animals.all()

    context = {
        'owner': owner,
        'animals_count': owner.animals_count,
        'animals': animals,
    }
    return render(request, 'owners/details-owner.html', context)

def rate_animal_view(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RatingForm()

    context = {'form': form}
    return render(request, 'rating/rate-animal.html', context)


def top_rated_view(request):
    animals_with_avg_rating = Animal.objects.annotate(avg_rating=Avg('ratings__value')).order_by('-avg_rating')

    context = {'animals_with_avg_rating': animals_with_avg_rating}
    for idx, animal in enumerate(animals_with_avg_rating, start=1):
        animal.place = idx

    return render(request, 'rating/top_rated.html', context)












