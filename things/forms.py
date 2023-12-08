"""Forms of the project."""
from django import forms

# Create your forms here.
class ThingForm(forms.Form):
    name = forms.CharField(label = "name", max_length = 35, required = True)
    description = forms.CharField(label = "description", widget = forms.Textarea, max_length = 120, required = False)
    quantity = forms.IntegerField(label = "quantity", widget = forms.NumberInput, min_value = 0, max_value=50)
    
