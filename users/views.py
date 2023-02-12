from django.shortcuts import redirect, render
from users.forms import LoginForm  
#from django.contrib.auth.models import user 
from users.models import CustomUser 
from django.contrib import messages
from .forms import RegistarionForm
from django.contrib.auth import authenticate
#from django.urls import reverse_lazy

# Create your views here.
def register(request):
	
	
		form = RegistarionForm()
		if request.method == 'POST':
			form = RegistarionForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username', 'first_name', 'last_name', 'email', 'password')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)





def login(request):
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				LoginForm(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)




