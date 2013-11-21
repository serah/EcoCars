from django import forms

class Save(forms.Form):
    state = forms.CharField(max_length=50)
    miles = forms.IntegerField()
    cartype = forms.IntegerField()
