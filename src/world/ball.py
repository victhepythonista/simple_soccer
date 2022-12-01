import pygame

import images 

from .entity import Entity 


class Ball(Entity):


	def __init__(self, pos ):
		Entity.__init__(self, pos , size = (20,20))
		self.speed = 0,0
		self.owner = None 
		self.ball_image = pygame.image.load(images.ball )
		self.SHOW_HITBOX = False

	def CustomDisplay(self , window , mouse_pos , events , keys ):
		window.blit(self.ball_image , self.pos)
	 



	def UpdatePos(self, new_pos):
		self.pos =  new_pos 
		self.x, self.y = new_pos 





class GoalLine(Entity):


	def __init__(self, pos , side):
		Entity.__init__(self, pos , size = (20,100), hitbox_color = (200,200,200))
		self.side = side
		 
