from django.db import models

# Create your models here.

class nodo ( models . Model ):
	nodo_name = models . CharField ( max_length = 45 )

	def __str__ (self):
		return self . nodo_name


class edge ( models . Model ):
	edge_weight = models . IntegerField ()
	connection = models.ManyToManyField ( nodo )

	
