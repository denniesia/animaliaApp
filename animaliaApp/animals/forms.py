from django import forms
from .models import Category, Animal, Owner, Rating

class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryForm(CategoryBaseForm):
    pass

class AnimalBaseForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class AnimalAddForm(AnimalBaseForm):
   class Meta(AnimalBaseForm.Meta):
       help_texts = {
           'birthdate': 'Format: YYYY-MM-DD (e.g. 2020-06-15)',
       }

class OwnerBaseForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class OwnerAddForm(OwnerBaseForm):
   pass

class OwnerEditForm(OwnerBaseForm):
    pass

class OwnerDeleteForm(OwnerBaseForm):
    pass

class DeleteAnimalForm(AnimalBaseForm):
   pass

class EditAnimalForm(AnimalBaseForm):
    pass

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'

    animal = forms.ModelChoiceField(
        queryset=Animal.objects.all(),
        empty_label="Choose an animal",
    )
    value = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 11)],
        widget=forms.Select,
        label="Rate the animal"
    )
