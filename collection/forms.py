from django.forms import ModelForm
from collection.models import Rocket

class RocketForm(ModelForm):
    class Meta:
        model = Rocket
        fields = ('name', 'description',)

