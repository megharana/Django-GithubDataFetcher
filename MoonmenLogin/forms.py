from django import forms

class HomeForm(forms.Form):
	name=forms.CharField()
class InfoHome(forms.Form):
	loginInfo=forms.CharField()