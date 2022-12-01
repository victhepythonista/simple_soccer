


import pygame,random ,math, time 

import tools , colors
from .entity import Entity 
from .ball import Ball ,GoalLine
from key_mapping import CONTROLS  

side = ["home", "away"]
 
class BasePlayer(Entity):


	def __init__(self, pos,size = (30,30 ), hitbox_color = (23,56,85) , side = "home" ):
		Entity.__init__(self, pos , size =size , hitbox_color = hitbox_color )
		self.side = side 
		self.HAS_BALL = False 
		self.SHOOTING = False
		self.world = None 
		self.shoot_timer = 0 
		self.shoot_limit = 100
		self.shoot_speed = 6
		self.last_touch_time = 0

	def Shoot(self):
		 
		w = self.world 
		self.HAS_BALL = False
		ball = self.world.GetEntities(Ball)[0]

		if tools.DistanceBetween(self.hitbox.center , ball.hitbox.center) > 30:
			return
		goal_line = [ g for g in w.GetEntities(GoalLine)  if g.side != self.side][0]
		# target_y= random.choice([goal_line.hitbox.y +  10 for  i in  range(10)])
		target_pos = goal_line.hitbox.center

		angle = tools.GetAngleBetween(   ball.hitbox.center, target_pos)

		vx = math.cos(math.radians(angle)) * self.shoot_speed
		vy = math.sin(math.radians(angle)) * self.shoot_speed


		self.SHOOTING = True 

		ball.vel = vx,vy
		self.last_touch_time = time.time()
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

		hitbox_color = colors.home_team if side == "home" else colors.away_team
		BasePlayer.__init__(self, pos , size = (30,30), hitbox_color = hitbox_color , side = side )
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
			bp_x = p[0] - 10
			bp_y = p[1] - 5
			self.ball_position = bp_x, bp_y


		if keys[c['up']] and self.hitbox.y > 110  :
			self.Move("up")
			p = list(self.hitbox.midtop)
			bp_x = p[0] - 5
			bp_y = p[1] - 10
			self.ball_position = bp_x, bp_y


		if keys[c['down']] and self.hitbox.midbottom[1] < 500  :
			self.Move("down")
			self.ball_position = self.hitbox.midbottom


		if keys[c['shoot']] and self.world :
			self.Shoot()

	 	

	def CustomDisplay(self , window , mouse_pos , events, keys ):
		if self.SHOOTING:
			self.shoot_timer += 1

			if self.shoot_timer > self.shoot_limit:
				self.shoot_timer = 0 
				self.SHOOTING = False
		if self.HAS_BALL:
			self.last_touch_time = time.time()

		self.HandleMovement(events, keys )


		pass 



class GoalKeeper(BasePlayer):


	def __init__(self,   goal_line  ):
		side = goal_line.side
		hitbox_color = colors.home_team if side == "home" else colors.away_team
		
		
		BasePlayer.__init__(self, goal_line.pos , size = (30,30), hitbox_color = hitbox_color )
		self.radar = None 
		self.radar_w  = 400 
		self.radar_h = 400 
		self.MOVE_LOCK = True
		self.vel = (0,2)
		self.goal_line = goal_line 

		if side == "away":
			bp = self.hitbox.topleft
			self.ball_position = bp[0] - 30, bp[1]
			x = 900 - self.width
			y = goal_line.hitbox.y +10 
			self.radar = pygame.Rect(self.x - 200, self.y - 100, self.radar_w,self.radar_h )
			self.UpdatePos((x,y))
		elif side == "home":
			bp = self.hitbox.topright
			self.ball_position = bp
			self.pos = goal_line.hitbox.midright
			self.radar = pygame.Rect(self.x ,self.y - 200 ,  self.radar_w , self.radar_h )

		self.ball_position = (self.hitbox.topright)


	def UpdateRadar(self ):
		if side == "away":
		 
			self.radar = pygame.Rect(self.x - 200, self.y - 100, 300,300 )
		elif side == "home":
			 
			self.radar = pygame.Rect(self.x ,self.y - 200 , 300,300 )
 
	def CustomDisplay(self , window , mouse_pos , events, keys ):
		self.UpdateRadar( )
	def Shoot(self):
		if not self.HAS_BALL:
			return

		self.HAS_BALL = False
		w = self.world


		ball = [b for b in w.GetEntities(Ball) ][0]

		target =   450, random.choice( [ i for i in range(100, 500)])
		angle = tools.GetAngleBetween(   ball.hitbox.center, target)

		vx = math.cos(math.radians(angle)) * self.shoot_speed
		vy = math.sin(math.radians(angle)) * self.shoot_speed
		self.SHOOTING = True 

		ball.vel = vx,vy
		self.last_touch_time = time.time()





