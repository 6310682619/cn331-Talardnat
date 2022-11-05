from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField()
	last_name = forms.CharField()

	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email", "password1", "password2")

	# def save(self, commit=True):
	# 	user = super(RegisterForm, self).save(commit=False)
	# 	user.email = self.cleaned_data["email"]
	# 	user.firstname = self.cleaned_data["firstname"]
	# 	user.lastname = self.cleaned_data["lastname"]
	# 	user.address = self.cleaned_data["address"]
	# 	if commit:
	# 		user.save()
	# 	return user

# class RegisterForm(UserCreationForm):
# 	firstname = forms.CharField(max_length=64,
#                                  required=True,
#                                  widget=forms.TextInput(attrs={'placeholder': 'First Name',}))

# 	lastname = forms.CharField(max_length=64,
#                                  required=True,
#                                  widget=forms.TextInput(attrs={'placeholder': 'Last Name',}))

# 	username = forms.CharField(max_length=64,
#                                  required=True,
#                                  widget=forms.TextInput(attrs={'placeholder': 'Last Name',}))

# 	email = forms.EmailField(max_length=64,
#                                  required=True,
#                                  widget=forms.TextInput(attrs={'placeholder': 'Last Name',}))

# 	password1 = forms.CharField(max_length=50,
#                                 required=True,
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password',
#                                                                   'data-toggle': 'password',
#                                                                   'id': 'password',
#                                                                   }))

# 	password2 = forms.CharField(max_length=50,
#                                 required=True,
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password',
#                                                                   'data-toggle': 'password',
#                                                                   'id': 'password',
#                                                                   }))

# 	class Meta:
# 		model = User
# 		fields = ('firstname','lastname', 'username', 'email', 'password1' ,'password2' )

# class ProfileForm(forms.ModelForm):
#     address = forms.CharField(widget=forms.Textarea())

#     class Meta:
#         model = Profile
#         fields = ('address',)

	# def clean(self):
	# 	firstname = self.cleaned_data["firstname"]
	# 	lastname = self.cleaned_data["lastname"]
	# 	address = self.cleaned_data["address"]

	# def save(self, commit=True):
	# 	user = super(RegisterForm, self).save(commit=False)
	# 	user.email = self.cleaned_data["email"]
		
	# 	if commit:
	# 		user.save()
	# 	return user