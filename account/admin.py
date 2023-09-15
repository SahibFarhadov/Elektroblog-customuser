from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import MyUser


class CustomUserAdmin(UserAdmin):
	add_form=CustomUserCreationForm
	form=CustomUserChangeForm
	model=MyUser
	list_display=("email","is_active","is_staff","is_superuser")
	fieldsets=(
		(None,{"fields":("email","password")}),
		("İcazələr",{"fields":("is_staff","is_active","groups","user_permissions")}),
	)

	add_fieldsets=(
		(None,{
			"classes": ("wide",),
			"fields": ("email","password1","password2","is_staff","is_active","groups","user_permissions")
		}),
	)
	ordering=('email',)

admin.site.register(MyUser,CustomUserAdmin)



