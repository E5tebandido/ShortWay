
from django.db import models

# Create your models here.

class route ( models . Model ):
	source_node = models . CharField ( max_length = 45 )
	target_node = models . CharField ( max_length = 45 )

	def __str__ ( self ):
		return self.source_node


class graph ( models . Model ):
	source_node = models . CharField ( max_length = 45 )
	target_node = models . CharField ( max_length = 45 )
	weight_edge = models . IntegerField ()

	def __str__ ( self ):
		return self.target_node

	def __str__ ( self ):
		return self.source_node



