
from .models import graph

class CreateGraph :

	def create () :
		thisgraph = graph . objects . all() . order_by ( 'source_node' )
		listgraph = []

		for elements in thisgraph :
			listgraph +=[( elements . source_node , elements . target_node , elements . weight_edge )]

		return listgraph

		
