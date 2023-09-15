from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import MyUser
from .forms import CreateUserForm

class UserCreateView(CreateView):
	form_class=CreateUserForm
	success_url='/'

