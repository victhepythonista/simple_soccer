

import math 
import pygame
import random
import time

from tools import DistanceBetween,OppositeSide , GetNow

from ui import GoalAnnouncement,Announcement 
from world import *
from sounds import GameSounds as GS


GOAL_LIMIT = 5
pitch_rect = pygame.Rect(0,100,900,400)
class GameManager:
	"""
	manages the game  mechanics and logics


	"""
	def __init__(self):
		self.scores = {"home":0 , "away":0}
		self.scores_file = "RESULTS.txt"
	def Manage(self, world ):
		# run the methods for managing the game
		# 

		ball = world.GetEntities(Ball)[0]
		players = world.GetEntities(Player)
		goal_keepers = world.GetEntities(GoalKeeper)
		goal_lines = world.GetEntities(GoalLine)


		self.BackendManagement(goal_keepers, ball , goal_lines, players )
		self.AssignPossesion(ball ,  players)
		
	def SaveScores(self):
		# save the game scores
		print("SAVING SCORES --")
		score = self.scores
		with open(self.scores_file, "a") as f:
			f.write(f"{GetNow()}-->    {score['home'] }   |    {score['away']}")

	def BackendManagement(self, goal_keepers, ball, goal_lines , players  ):
		# DETECT BALL OUTSIDE THE PITCH RECT 
		if not ball.hitbox.colliderect( pitch_rect):
			last_to_touch = self.GetLastTouch(players) 
			# reset the game
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

				self.scores[opp]+= 1 # increase the goals for the player
				if self.scores[opp] >= GOAL_LIMIT:
					# Announce  a goal has been scored 
					Announcement(f"WINNER   {opp}!!    ").show()
					self.SaveScores() # save scores
					GS.play("score_goal") # play the goal scored sound

					self.scores["home"] = 0
					self.scores["away"] = 0
					self.Reset(side , players, ball, goal_keepers , goal_lines)
					return
				GoalAnnouncement().show() # show the goal announcement
				ball.vel = (0,0) # change the ball velocity

				# reset the game
				self.Reset(side, players, ball , goal_keepers , goal_lines)
				print("GOAAAAALL   ", opp)


				return 



		line = goal_lines[1]

		# check for collisions between goalkeepers and the nball 
		for g in goal_keepers:
			 

			gc = g.hitbox.center
			bc = ball.hitbox.center
			g.HAS_BALL = False
			g.UpdateRadar()
			# check if the goalkeeper has collided with the ball 
			if g.hitbox.colliderect(ball.hitbox):
				g.HAS_BALL = True

				if g.HAS_BALL:
					g.Shoot() # shoot the ball 
					g.HAS_BALL = False
					GS.play("deflect")

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
 		# get the strikers
		strikers = [ p for p in players if not isinstance(p, GoalKeeper) ]

		# get the sides 
		sides = [p.side for p in goal_keepers]

		# adjust side appropriately 
		# ! for the side bug issue -->FIXES IT !!
		if sides[0] == sides[1]:
			print("SAME SIDE")
			strikers[1].side  = OppositeSide(sides[0])
		ball.vel == (0,0)
		line = goal_lines[0]
		home_goal_line = goal_lines[1] if line.side == "away" else line 
		away_goal_line = goal_lines[1] if line.side == "home" else line 

		goal_limit = line.hitbox.y, line.hitbox.bottomright[1] 

		# iterate the strikeer and update their position
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

		# check if the player is within the correct distance to 
		# possess the ball 
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

if __name__ == '__main__':
	# testing..
	GameManager().SaveScores()