
from .models import source , target


class CreateDict :

	graph = {}
	global this_source_node 
	global name_first_node_sublist

	def createDict ( source_n , taget_n ):
		nodes = source . objects . all()
		selected_node = source . objects . get ( id = source_n )
		connected_nodes_with_selected = target . objects . filter ( source_node_id = selected_node )  
		graphlist = {}
		subgraphlist = {}
		auxlist = {}
		
		iterator = 0
		id_source = source_n

		for connections in connected_nodes_with_selected :
			subgraphlist [ connections . target_node ] = connections . weight_edge
			iterator = iterator + 1

			if iterator == 1 :
				name_first_node_sublist = connections . target_node

			if id_source == source_n :
				graphlist [ selected_node . source_node ] = subgraphlist
				id_source = 0


		for connections in connected_nodes_with_selected :
			if id_source != source_n :
				next_node = target . objects . filter ( id = connected_nodes_with_selected )

				for next in next_node :
					subgraphlist [ next . target_node ] = next . weight_edge	

				if name_first_node_sublist == connections . target_node :
					graphlist [ connections . target_node ] = subgraphlist
			
			
			



		print (graphlist)

		
		
			
