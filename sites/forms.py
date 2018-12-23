from django import forms

class UploadSiteForm(forms.Form):
    sitename = forms.CharField(label='Sitename', max_length=30)
    url = forms.CharField(label='URL', max_length=30)
    description = forms.CharField(label='Description', max_length=30)