from django import forms

class ExampleForm(forms.Form):
    """Simple example form"""
    example_field = forms.CharField(label='Example Field')