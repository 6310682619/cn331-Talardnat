from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField()
	last_name = forms.CharField()
	address = forms.CharField()
	city = forms.CharField()
	state = forms.CharField()
	zip = forms.IntegerField()
	phone = forms.IntegerField()

	class Meta:
		model = User
		fields = ["first_name", "last_name", "username", "email", "password1", "password2", "address", "city", "state", "zip", "phone"]