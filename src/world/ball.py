import pygame

import images 

from .entity import Entity 


class Ball(Entity): 
	"""

	bALL 

	used to play the game.. possessed by a player """

	def __init__(self, pos ):
		Entity.__init__(self, pos , size = (10,10))
		self.vel = 0,0
		self.owner = None 
		self.ball_image = pygame.image.load(images.ball )
		self.SHOW_HITBOX = False

	def CustomDisplay(self , window , mouse_pos , events , keys ):
		window.blit(self.ball_image , self.pos)

		
	 







class GoalLine(Entity):

	"""

	OBJECT used to represent the goals....used to detect  a goal scored

	"""
	def __init__(self, pos , side):
		Entity.__init__(self, pos , size = (20,100), hitbox_color = (200,200,200))
		self.side = side
		 

	def __repr__(self):
		return "GOAL LINE -/ " +  self.side

