"""

RUN THIS FILE TO PLAY THE GAME 

RESULTS IN : RESULTS.txt




"""


import pygame, time  , math , random

import colors , images
from buttons import  SimpleButton
from screen import Screen
from tools import write_on_screen as wos , iload 
from animation import PointAnimation
 
from world import World , Entity ,Ball ,Player ,AI_Player,GoalLine ,GoalKeeper
from game_manager import GameManager


 
SIDES = "home","away"
 

class GameScreen(Screen):
	"""
	Screen class that contains all the games objects and displays them 

	"""
	def __init__(self):
		Screen.__init__(self)

		self.buttons = [ 
		SimpleButton( (200,20), self.GoHome, "BACK", (120,40) ), 

		 ]
		self.world = World() 

		# LISTS OF THE OBJECTS IN THE GAME
		goal_lines= []
		goal_keepers = [] 
		home_players = [] 
		away_players = [] 
		players  = [] 

		# initialize sides 
		for s in SIDES:
			if s == "home":
				# MAKE OBJECTS FOR HOME SIDE
				goal_line = GoalLine((-10, 250 ),s) 
				keeper = GoalKeeper( s, goal_line)
				player = Player((200,450,), "striker",side = s)
				

				goal_lines.append(goal_line)
				goal_keepers.append(keeper)
				home_players += [player, keeper]

			elif s == "away":
				# MAKE OBJECTS FOR  AWAY SIDE

				goal_line = GoalLine((890, 250) , s)
				keeper = GoalKeeper( s, goal_line)
				player = Player((400,450,), "striker",side = s)


				goal_lines.append(goal_line)
				goal_keepers.append(keeper)
				away_players += [ player , keeper]


		players = home_players + away_players 

		ball = Ball((200,100))
		print("goal_keepers  _-- ",goal_keepers)

		 
		for p in players:
			# update the world attribute in the players
			p.world = self.world

	 	
		self.world.AddEntities([ball  ] + players  + goal_lines) # add the world objects
		self.game_manager = GameManager() 
		self.game_manager.Reset(random.choice(SIDES) , players , ball , goal_keepers , goal_lines)


	def GoHome(self):
		# go back to home screen 
		self.running = False 
		HomeScreen().show()

	 
	def ShowScores(self):
		# write the current scores onto the screen 
		scores = self.game_manager.scores
		board_pos  = 480,20
		self.window.blit(iload(images.score_board), board_pos)
		wos(f"{scores['home']}  {scores['away']}   " ,( board_pos[0] + 160 , board_pos[1] + 15) , self.window , (0,30,60) , 40)




 
	def display_widgets(self):
		# display the screen items 
		self.window.fill("gray")

		ball = self.world.GetEntities(Ball)[0]
		players = self.world.GetEntities(Player)
		goal_keepers = self.world.GetEntities(GoalKeeper)
		goal_lines = self.world.GetEntities(GoalLine)

		# display the pitch
		self.window.blit(iload(images.pitch), (0, 100))

		# show the current scores
		self.ShowScores()

		# display the buttons
		for b in self.buttons:
			b.show(self.window, pygame.mouse.get_pos() , self.events)

		self.game_manager.Manage(self.world)
		self.world.show(self.window , self.events , pygame.mouse.get_pos(), self.keys)



class  HelpScreen(Screen):
	"""

	SCREEN for showing Help information, rules and CONTROLS"""
	def __init__(self):
		Screen.__init__(self)

		self.buttons = [ 
	 
		SimpleButton( (0,0), self.BackHome , "BACK" , (200, 50) )


		 ]

	def BackHome(self):
		# go back to Home screen
		self.running = False
		HomeScreen().show()

	def display_widgets(self):

		self.window.fill(pygame.Color("white")) 
		#message, position, window, color, fontsize,

		self.window.blit(iload(images.help_menu), (200,0))

		for b in self.buttons:
			b.show(self.window, pygame.mouse.get_pos() , self.events)

# home screen 
class HomeScreen(Screen):
	def __init__(self):
		Screen.__init__(self)

		self.buttons = [ 
		SimpleButton( (500,150), self.PlayGame, "START", (240, 50) ),
		SimpleButton( (500,250), self.ShowHelpMenu, "HELP" , (240, 50) ),
		SimpleButton( (500,350), self.exit, "EXIT" , (240, 50) )


		 ]




	def ShowHelpMenu(self):
		# display the help menu
		self.running = False
		HelpScreen().show()

	def PlayGame(self):
		# start the game
		print("-starting a game ..")
		self.running = False 

		GameScreen().show() # display the game screen
		pass 

	def display_widgets(self):

		self.window.fill(pygame.Color("white")) 

		# display the background image		
		self.window.blit(iload(images.home_bg) , (0,0))
		wos(" SIMPLE SOCCER " ,( 200,50) , self.window , (0,0,0) , 50 , "Lucida console")
		
		# show the buttons
		for b in self.buttons:
			b.show(self.window, pygame.mouse.get_pos() , self.events)

if __name__ == '__main__':
	# START THE GAME 
	HomeScreen().show()