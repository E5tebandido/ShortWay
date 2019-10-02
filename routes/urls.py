
from django.urls import path

from . import views

urlpatterns = [
	# /routes/
	path ( '' , views.index , name='index' ),

]