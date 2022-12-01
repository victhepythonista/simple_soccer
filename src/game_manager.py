

import math 
import pygame


from ui import GoalAnnouncement 
from world import GoalKeeper


def DistanceBetween(p1, p2):
	distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
	return distance
class GameManager:
	"""
	manages the game  

	"""
	def __init__(self):
		self.scores = {"home":0 , "away":0}
	def Manage(self,  ball , players,  goal_lines ):
		self.AssignPossesion(ball ,  players)
		self.DetectGoal(ball,  goal_lines, players)
		


	def Reset(self, side , players, ball ):
		strikers = [ p for p in players if not isinstance(p, GoalKeeper) ]
		ball.pos = 450,200 
		GoalAnnouncement().show()







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
	 
	 
		ind =  location_diff.index(min(location_diff))
		if not ind <= 45:
			return 

		player =  players[ind]
		player.HAS_BALL = True 
		ball.UpdatePos(  player.ball_position)
		ball.speed = (0,0)

