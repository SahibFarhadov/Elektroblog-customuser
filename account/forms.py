from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import MyUser


# Admin site ucun user formlari
class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model=MyUser
		fields=('email',)

class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model=MyUser
		fields=('email',)

# Admin site ucun user formlari sonu

# Admin site-den kenar user formu
class CreateUserForm(ModelForm):
	class Meta:
		model=MyUser
		fields=["email","password"]