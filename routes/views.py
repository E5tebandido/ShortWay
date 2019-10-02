
from django.shortcuts import  render

from .models import nodo
from routes import dijkstra


def index ( request ):
	"""
	function that render the graph form 
	"""	
	if request.method == "POST":
		data = request.POST
		
		context = {
			'var': dijkstra.Graph.dijkstra(data.get("source"))

		}	
		return render ( request , 'routes/index.html' , context )
	else:
		thisnodos = nodo.objects.all()
		context = {
			'nodos': thisnodos
		}
		return render ( request , 'routes/index.html' , context )




	
