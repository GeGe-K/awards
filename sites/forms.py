from django import forms
from .models import Project, Review
class UploadSiteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','pub_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['project']