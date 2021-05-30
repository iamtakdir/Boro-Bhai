from .models import Video
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields =['title', 'url', 'youtube_id']

class SearchForm (forms.Form):
    search= forms.CharField(max_length=300 , label='Search For Resources ')