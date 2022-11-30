



class World:



	def __init__(self ):
		self.focal_poins = [] 
		self.entities = [] 


	def AddEntities(self, ls):
		self.entities += ls 

	def show(self, window, events, mouse_pos ):
		for ent in self.entities:
			ent.show(window , events, mouse_pos)
			