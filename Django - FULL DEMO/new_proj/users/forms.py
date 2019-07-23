from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class RFPAuthForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ['username','password']
	def __init__(self, *args, **kwargs):
		super(RFPAuthForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
		self.fields['username'].label = False
		self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'})	
		self.fields['password'].label = False


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		widgets = {
			'username': forms.TextInput(
				attrs={'placeholder': 'Username', 'class': 'form-control'}),
		}
	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm password'})