

import math 
import pygame
import random

from tools import DistanceBetween,OppositeSide 

from ui import GoalAnnouncement,Announcement 
from world import *
from sounds import GameSounds as GS


GOAL_LIMIT = 5
pitch_rect = pygame.Rect(0,100,900,400)
class GameManager:
	"""
	manages the game  mechanics and logic 


	"""
	def __init__(self):
		self.scores = {"home":0 , "away":0}
	def Manage(self, world ):
		# 

		ball = world.GetEntities(Ball)[0]
		players = world.GetEntities(Player)
		goal_keepers = world.GetEntities(GoalKeeper)
		goal_lines = world.GetEntities(GoalLine)


		self.BackendManagement(goal_keepers, ball , goal_lines, players )
		self.AssignPossesion(ball ,  players)
		

	def BackendManagement(self, goal_keepers, ball, goal_lines , players  ):
		# DETECT BALL OUTSIDE THE PITCH RECT 

		if not ball.hitbox.colliderect( pitch_rect):
			last_to_touch = self.GetLastTouch(players)
			
			self.Reset( OppositeSide(last_to_touch), players, ball,goal_keepers, goal_lines, goal = False )
			GS.play("ball_out")
			return

		# DETECT A GOAL 
		for g in goal_lines:
			if g.hitbox.colliderect(ball.hitbox):
				side = g.side 

				sides = ["away", "home"]
				sides.remove(side)
				opp = sides[0]
				GS.play("score_goal")

				self.scores[opp]+= 1
				if self.scores[opp] >= GOAL_LIMIT:
					# Announce  a goal has been scored 
					Announcement(f"WINNER   {opp}!!    ").show()
					GS.play("score_goal")

					self.scores["home"] = 0
					self.scores["away"] = 0
					self.Reset(side , players, ball, goal_keepers , goal_lines)
					return
				GoalAnnouncement().show()
				ball.vel = (0,0)
				self.Reset(side, players, ball , goal_keepers , goal_lines)
				print("GOAAAAALL   ", opp)


				return 



		line = goal_lines[1]

		# check for collisions between goalkeepers and the nball 
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

		

	def Reset(self, side , players, ball, goal_keepers , goal_lines ,goal = True  ):
		# reset the positions of the players and goalkeepers
		"""
		side -> side that had the ball last
		 """

		print("GOAL lineS -->" , goal_lines)
		print("goal_keeper  ./ s", goal_keepers)
		strikers = [ p for p in players if not isinstance(p, GoalKeeper) ]
		sides = [p.side for p in goal_keepers]
		if sides[0] == sides[1]:
			print("SAME SIDE")
			strikers[1].side  = OppositeSide(sides[0])
		ball.vel == (0,0)
		line = goal_lines[0]
		home_goal_line = goal_lines[1] if line.side == "away" else line 
		away_goal_line = goal_lines[1] if line.side == "home" else line 

		goal_limit = line.hitbox.y, line.hitbox.bottomright[1] 

		for p in strikers:
			w = p.world
			if p.side == "home":

				p.UpdatePos((300,300))



			if p.side == "away":
				p.UpdatePos((700,300))

		p = [p for p in strikers if p.side == side][0]

		# give ball to the faulted/ fouled side 
		striker= [p for p in  strikers if p.side != side and not isinstance(p,GoalKeeper)][0]
		print("STRIKER : ",striker)
			
		strikers = [ p for p in players if not isinstance(p, GoalKeeper) ]
		p = [p for p in strikers if p.side == side][0]

		ball.UpdatePos(p.hitbox.topright)

 	
		print("RESET POST BALL  VEL ", ball.vel , "\n BALL POS ",ball.pos)
		ball.vel = (0,0)

	def GetLastTouch(self, players):
		# get the last side to posses the ball 

		ps = players
		touch_times =  [ p.last_touch_time for p in players ]
		most = max(touch_times)
		most_index = touch_times.index(most) - 1
		last_touch = ps[most_index].side
		return last_touch

 

		
 
 
	def AssignPossesion(self, ball , players):
		# assign possesion to a player who is closest to the ball 
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

