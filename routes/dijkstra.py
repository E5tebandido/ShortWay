
from .models import nodo

class Graph():

	"""
	- def nodos method void: is a method that implements the algorithm method in the model class
	"""


	def dijkstra ( self ):
		"""
		params:	 
		"""
		nodes = list(nodo.objects.all())
		
		for source_nodo in nodes:
			dict_source = {}
			for target_nodo in nodes:
				if source_nodo == target_nodo
					dict_source[target_nodo] = 0
				else:
					dict_source[target_nodo] = float('inf')
			self.distances[source_nodo] = dict_source

		for oneNode in nodes: #start algorithm
			listNode = []
			for node in nodes: listNode.append(node)


			while len(listQ) != 0:
				nodeauxiliar = 0
				min = float("inf")
				for node_listnode in listNode:
					if self.distances[oneNode][node_listnode] <= min :
						min = self.distances[oneNode][node_listnode] 
						nodeauxiliar = node_listnode

				listNode.remove(nodeauxilar)

				neighbors = list(nodo.objects.all()) 

				for neighbor in neighbors:
					neighborauxiliar = self.Graph[nodeauxiliar][neighbor]['weight']
					alt = self.distances[oneNode][nodeauxilar] + neighbor
					if alt < self.distances[oneNode][neighbor]:
						self.distances[oneNode][neighbor] = alt

	return self.distances


	def create_network( self, source_nodo , target_nodo , weight ):

		source= nodo.objects.get(id = source_nodo)
		target= nodo.objects.get(id = target_nodo)

		self.Graph = nx.DiGraph()
		count = len(source_nodo)

		listedges = []

		for i in range(0, count):
			listedges.append((source, target, weight[i]))

		self.Graph.add_weighted_edges_from(listedges)
		return self.Graph
	

	
