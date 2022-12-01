

import math 
import pygame


from tools import DistanceBetween

from ui import GoalAnnouncement 
from world import GoalKeeper


pitch_rect = pygame.Rect(0,100,900,400)
class GameManager:
	"""
	manages the game  

	"""
	def __init__(self):
		self.scores = {"home":0 , "away":0}
	def Manage(self,  ball , players,  goal_lines ):
		self.AssignPossesion(ball ,  players)
		self.DetectGoal(ball,  goal_lines, players)
		


	def Reset(self, side , players, ball ,goal = True  ):
		strikers = [ p for p in players if not isinstance(p, GoalKeeper) ]

		if   goal:
			GoalAnnouncement().show()


		for p in strikers:
			if p.side == "home":
				p.UpdatePos((300,300))
				if side != p.side:
					ball.UpdatePos(p.hitbox.topright)
			if p.side == "away":
				p.UpdatePos((700,300))
				if side != p.side:
					ball.UpdatePos(p.hitbox.topright)



 
	def DetectGoal(self , ball , goal_lines, players):
		for g in goal_lines:
			if g.hitbox.colliderect(ball.hitbox):
				side = g.side 
				self.scores[side]+= 1
				self.Reset(side, players, ball )
				return 




 
	def AssignPossesion(self, ball , players):
		positions = [p.hitbox.center  for p in players]
		ball_p =  ball.hitbox.center
		touch_distance = 50

		location_diff = [  DistanceBetween(ball_p , p)  for  p in  positions ]
		dist  = min(location_diff)
	 
		ind =  location_diff.index(dist)
		if  dist > 40 :
			return 


		player =  players[ind]

		if  player.SHOOTING:
			return 

		# print("ASSIGNED POSTION TO ", player)

		player.HAS_BALL = True 
		ball.UpdatePos(  player.ball_position)
		ball.vel= (0,0)

		for p in players:
			if p != player:
				p.HAS_BALL = False

