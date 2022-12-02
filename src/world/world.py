



class World:

	"""

	CONTAINER FOR EVERY OBJECT in the game..everything  .. 

	"""

	def __init__(self ):
		self.focal_poins = [] 
		self.entities = [] 

	# add  entities to the worlds
	def AddEntities(self, ls):
		self.entities += ls 

	# get entities of the same object type
	def GetEntities(self, inst):
		# get a list of entities with a similar instance 
		l = [] 
		for ent in self.entities:
			if isinstance(ent , inst):
				l.append(ent)
		return l

	# show the entitites
	def show(self, window, events, mouse_pos, keys  ):
		for ent in self.entities:
			ent.show(window , events, mouse_pos , keys)
			