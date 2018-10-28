from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.http import HttpResponse

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created! You are now able to login')
			return redirect('login')
	else:
		form =UserRegisterForm()
	return render(request,'filesystem/register.html',{'form':form})

class ActivateUser(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            request.session.modified = True


@login_required
def filesystem(request):
	return render(request,'filesystem/files.html',{})
