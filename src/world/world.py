



class World:



	def __init__(self ):
		self.focal_poins = [] 
		self.entities = [] 


	def AddEntities(self, ls):
		self.entities += ls 


	def GetEntities(self, inst):
		# get a list of entities with a similar instance 
		l = [] 
		for ent in self.entities:
			if isinstance(ent , inst):
				l.append(ent)
		return l
	def show(self, window, events, mouse_pos, keys  ):
		for ent in self.entities:
			ent.show(window , events, mouse_pos , keys)
			