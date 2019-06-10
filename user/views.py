from django.shortcuts import render
from django.contrib.auth.forms import (
	UserCreationForm,
	)
from django.urls import(
	reverse_lazy,
	)
from django.views.generic import(
	CreateView,
	)
from django.contrib.auth.models import User

# Create your views here.
class RegisterView(CreateView):
	template_name = 'user/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy(
		'teacher_rating:existing_chair')

def  CurrentUser(request, user_id):
	user = User.objects.get(pk=user_id)
	username = user.username
	if username != "AnonymousUser":
		context ={'user':username}
	render(request, 'base.html', context)
