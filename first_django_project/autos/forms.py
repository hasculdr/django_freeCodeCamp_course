from django.forms import ModelForm
from autos.models import Auto, Manufacturer

class MakerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'

