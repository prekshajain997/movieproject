from django import forms
from movieapp.models import Moviedetails


class MoviedetailsForm(forms.ModelForm):
     class Meta:
     	model= Moviedetails
     	fields = ('releasedate','moviename','hero','heroine','rating')