from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	firstname = forms.CharField(label = "Firstname")
	lastname = forms.CharField(label = "Lastname")
	address = forms.CharField(label = "Address")

	class Meta:
		model = User
		fields = ("firstname", "lastname", "address", "username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.firstname = self.cleaned_data["firstname"]
		user.lastname = self.cleaned_data["lastname"]
		user.address = self.cleaned_data["address"]
		if commit:
			user.save()
		return user