from django import forms 

class UrlForm(forms.Form):
    original_url = forms.URLField()
    suggested_url_suffix = forms.CharField(required = False)
    slug = forms.CharField(widget = forms.HiddenInput(), required = False)
    generated_url = forms.URLField(widget = forms.HiddenInput(), required = False)




