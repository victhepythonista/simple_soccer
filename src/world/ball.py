

from .entity import Entity 


class Ball(Entity):


	def __init__(self, pos ):
		Entity.__init__(self, pos , size = (50,50))

		
