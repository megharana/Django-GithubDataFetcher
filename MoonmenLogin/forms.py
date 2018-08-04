from django import forms

class seachUser_form(forms.Form):
	name=forms.CharField()
class saveData_form(forms.Form):
	loginInfo=forms.CharField()