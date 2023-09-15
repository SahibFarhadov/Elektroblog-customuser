from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class MyUser(AbstractUser):
	class Meta:
		verbose_name="İstifadəçi"
		verbose_name_plural="İstifadəçilər"
	username=None
	email=models.EmailField(_("Elektron poçt"), unique=True)
	USERNAME_FIELD='email'
	REQUIRED_FIELDS=[]

	objects=CustomUserManager()

	def __str__(self):
		return self.email
	