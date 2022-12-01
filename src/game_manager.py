

import math 
import pygame
import random

from tools import DistanceBetween

from ui import GoalAnnouncement,Announcement 
from world import *


GOAL_LIMIT = 5
pitch_rect = pygame.Rect(0,100,900,400)
class GameManager:
	"""
	manages the game  

	"""
	def __init__(self):
		self.scores = {"home":0 , "away":0}
	def Manage(self, world ):


		ball = world.GetEntities(Ball)[0]
		players = world.GetEntities(Player)
		goal_keepers = world.GetEntities(GoalKeeper)
		goal_lines = world.GetEntities(GoalLine)


		self.BackendManagement(goal_keepers, ball , goal_lines, players )
		self.AssignPossesion(ball ,  players)
		
	def BackendManagement(self, goal_keepers, ball, goal_lines , players  ):

		# DETECT A GOAL 
		for g in goal_lines:
			if g.hitbox.colliderect(ball.hitbox):
				side = g.side 

				sides = ["away", "home"]
				sides.remove(side)
				opp = sides[0]

				self.scores[opp]+= 1
				if self.scores[opp] >= GOAL_LIMIT:
					Announcement(f"WINNER   {opp}!!    ").show()
					self.scores["home"] = 0
					self.scores["away"] = 0
					self.Reset(side , players, ball)
					return
				GoalAnnouncement().show()

				self.Reset(side, players, ball )
				print("GOAAAAALL   ", opp)


				return 



		line = goal_lines[1]
		for g in goal_keepers:
			 

			gc = g.hitbox.center
			bc = ball.hitbox.center
			g.HAS_BALL = False
			if g.hitbox.colliderect(ball.hitbox):
				g.HAS_BALL = True

				if g.HAS_BALL:
					g.Shoot()
					g.HAS_BALL = False

			diff = gc[1] - bc[1]

			# check if within limits 
			if g.radar.colliderect(ball.hitbox):
				if -40 <  diff <  40 :
					if diff >=  0 :
						g.Move("up")
					else:
						g.Move("down")

		if ball.hitbox.colliderect( pitch_rect):
			return
			print("BALL OFF PITCH")
		side ="away" if  self.GetLastTouch(players) == "home" else "home"
		self.Reset(side, players, ball, goal = False )

	def Reset(self, side , players, ball ,goal = True  ):
		strikers = [ p for p in players if not isinstance(p, GoalKeeper) ]
		ball.vel == (0,0)
		p = [p for p in players if p.side == side][0]
		ball.UpdatePos(p.hitbox.topright)
		for p in strikers:
			w = p.world
			if p.side == "home":

				p.UpdatePos((300,300))

			if p.side == "away":
				p.UpdatePos((700,300))
			

		goal_line = w.GetEntities(GoalLine)[0]
		goal_keepers = w.GetEntities(GoalKeeper)
		 

	def GetLastTouch(self, players):

		ps = players
		touch_times =  [ p.last_touch_time for p in players ]
		most = min(touch_times)
		most_index = touch_times.index(most) - 1
		last_touch = ps[most_index].side
		return last_touch

 

		
 
 
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

