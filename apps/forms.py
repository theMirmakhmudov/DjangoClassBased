from django.forms import ModelForm
from apps.models import People


class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = '__all__'

