from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
	""" Ferdi istifadeci meneceri """

	# Yeni istifadecinin yaradilmasi funksiyasi
	def create_user(self,email,password,**extra_fields):
		if not email:
			raise ValueError(_("Elektron poçt ünvanı daxil edilməlidir."))
		email=self.normalize_email(email)
		user=self.model(email=email,**extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self,email,password,**extra_fields):
		"""" Super istifadecinin yaradilmasi funksiyasi """

		extra_fields.setdefault("is_staff",True)
		extra_fields.setdefault("is_active",True)
		extra_fields.setdefault("is_superuser",True)

		if extra_fields.get("is_staff") is not True:
			raise ValueError(_("Superistifadəçi is_staff=True olmalıdır"))
		if extra_fields.get("is_superuser") is not True:
			raise ValueError(_("Superistifadəçi is_superuser=True olmalıdır"))

		return self.create_user(email,password,**extra_fields)