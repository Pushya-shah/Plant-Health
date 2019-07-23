from django.shortcuts import render,redirect
from .forms import UserRegisterForm

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		x = form.fields['username']
		x.label = False
		x.help_text = ""
		x = form.fields['email']
		x.label = False
		x = form.fields['password1']
		x.label = False
		x.help_text = ""
		x = form.fields['password2']
		x.label = False
		x.help_text = ""
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserRegisterForm()
		x = form.fields['username']
		x.label = False
		x.help_text = ""
		x = form.fields['email']
		x.label = False
		x = form.fields['password1']
		x.label = False
		x.help_text = ""
		x = form.fields['password2']
		x.label = False
		x.help_text = ""
	return render(request,'users/register.html',{'form':form})

