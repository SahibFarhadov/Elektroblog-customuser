from django.urls import path
from .views import UserCreateView
from django.views.generic import TemplateView


urlpatterns=[
	path("hesab/yarat",UserCreateView.as_view(template_name='account/istifadeci_yarat.html')),
	path("",TemplateView.as_view(template_name='account/index.html')),
]