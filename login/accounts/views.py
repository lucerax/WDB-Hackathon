from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponse
from .forms import UserProfileForm


# Create your views here.
def indexView(request):
	return render(request, 'index.html')

@login_required
def dashboardView(request):
	return render(request, 'registration/dashboard.html')

def registerView(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		profile_form = UserProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user = form.save()

			profile = profile_form.save(commit = False)
			profile.user = user

			profile.save()


			return redirect('login_url')
	else:
		form = UserCreationForm()
		profile_form = UserProfileForm()
	return render(request, 'registration/register.html', {'form': form, 'profile_form': profile_form})
@login_required
def favoritesView(request):
	return render(request, 'recipes/favoritesView.html')




