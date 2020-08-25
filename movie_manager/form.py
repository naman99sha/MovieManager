from django import forms
from .models import Entry
class MovieForm(forms.ModelForm):
	class Meta():
		model=Entry
		fields=['moviePoster','movieName','movieDescription','releaseDate']