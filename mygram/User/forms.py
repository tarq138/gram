from django.forms import ModelForm
from .models import ProfileImage


class AddImage(ModelForm):
    class Meta:
        model = ProfileImage
        fields = ['image', 'is_main']
