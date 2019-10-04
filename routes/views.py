
from django.shortcuts import  render

from .models import graph
from routes import  dijkstra


def index ( request ):
	"""
	function that render the graph form 
	"""	
	if request.method == "POST":
		data = request.POST
		
		context = {
			'var': dijkstra.processroute ( data.get ('source'), data.get ('target'))

		}	
		return render ( request , 'routes/index.html' , context )
	else:
		source_node = graph.objects.all()
		target_node = graph.objects.all() 
		context = {
			'source': source_node,
			'target': target_node		
		}
		return render ( request , 'routes/index.html' , context )




	
