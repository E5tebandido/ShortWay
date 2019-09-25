from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hola mundi, you are at the routes index.")