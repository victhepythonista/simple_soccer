


import pygame

import tools 
from .entity import Entity 
from .ball import Ball 
from key_mapping import CONTROLS  

 
class BasePlayer(Entity):


	def __init__(self, pos,size = (50,50 ), hitbox_color = (23,56,85) , side = "home" ):
		Entity.__init__(self, pos , size =size , hitbox_color = hitbox_color )
		self.side = side 
		self.HAS_BALL = False 
		self.world = None 



	def Shoot(self):
		ball = self.world.GetEntities(Ball)[0]
		print(ball.hitbox.midleft)
		
class AI_Player(BasePlayer):


	def __init__(self, pos,role , ball  ):
		BasePlayer.__init__(self, pos , size = (50,50), hitbox_color = (20,2,9) )
		self.role = role
		self.ball =  ball 
		self.MOVE_LOCK = False 
		self.vel = (0,0)
		self.angle = 0




	 
	def CustomDisplay(self , window , mouse_pos , events , keys):
		
		self.Play()


	def Play(self):
		bp =self.ball.hitbox.center # ball position 
		center = self.hitbox.center

		angle = tools.GetAngleBetween(center , bp )
		focus_point = tools.GetPointOnCirc(angle ,  center , 1)
		self.vel = focus_point





class Player(BasePlayer):


	def __init__(self, pos,role,  side  = "home" ):

		hitbox_color = pygame.Color("orange") if side == "home" else pygame.Color("cyan")
		BasePlayer.__init__(self, pos , size = (50,50), hitbox_color = hitbox_color , side = side )
		self.role = role
		self.MOVE_LOCK = True
		self.side = side
		self.vel =  (2,2)
		self.ball_position = (self.hitbox.topright)

		self.touch_distance =  40



	def HandleMovement(self, events, keys ):
		if [] ==  keys:
			return 

		c = CONTROLS[self.side]
		if keys[c['right']] and self.hitbox.topright[0] < 900 :
			self.Move("right")
			self.ball_position = self.hitbox.midright


		if keys[c['left']]  and self.hitbox.topleft[0] > 0  :
			self.Move("left")
			p = list(self.hitbox.midleft)
			p[0] = p[0] - 25 
			self.ball_position = p  


		if keys[c['up']] and self.hitbox.y > 110  :
			self.Move("up")
			p = list(self.hitbox.midtop)
			p[1] = p[1] - 25 
			self.ball_position = p  


		if keys[c['down']] and self.hitbox.midbottom[1] < 500  :
			self.Move("down")
			self.ball_position = self.hitbox.midbottom


		if keys[c['shoot']] and self.world :
			self.Shoot()

	 	

	def CustomDisplay(self , window , mouse_pos , events, keys ):
		self.HandleMovement(events, keys )


		pass 



class GoalKeeper(BasePlayer):


	def __init__(self,   goal_line  ):
		side = goal_line.side
		
		BasePlayer.__init__(self, goal_line.pos , size = (50,50), hitbox_color = (3,6,65) )


		self.MOVE_LOCK = True
		self.vel = (0,0)
		self.goal_line = goal_line 

		if side == "away":
			bp = self.hitbox.topleft
			self.ball_position = bp[0] - 30, bp[1]
			self.pos = goal_line.hitbox.midleft
		elif side == "home":
			bp = self.hitbox.topright
			self.ball_position = bp
			self.pos = goal_line.hitbox.midright
		self.ball_position = (self.hitbox.topright)


		
