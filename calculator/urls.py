"""URL shemes for 'calculator' app."""

from . import views
from django.urls import path


app_name = "calculator"
urlpatterns = [
	# Home page.
	path('', views.calculate, name="calculate"),
]