import pygame, time  , math , random



import colors , images
from buttons import UIButton , SimpleButton
from screen import Screen
from tools import write_on_screen as wos , iload 
from animation import PointAnimation
 
from world import World , Entity ,Ball ,Player ,AI_Player,GoalLine ,GoalKeeper
from game_manager import GameManager


 

class ScreenManager:

	def __init__(self):

		self.screens = []



class GameScreen(Screen):
	def __init__(self):
		Screen.__init__(self)

		self.entities = [] 
		self.paused = False 
		self.buttons = [ 
		SimpleButton( (200,20), self.GoHome, "BACK", (120,40) ),

		 ]
		self.world = World() 
		goal_lines = [GoalLine((-10, 250),"home") , GoalLine((890,250), "away")]
		ball = Ball((200,100))
		goalies = [GoalKeeper(goal_lines[0]),GoalKeeper(goal_lines[1])  ]
		for g in goalies:
			g.world = self.world
		home_players = [Player((100,200,), "striker", side = "home"),]
		away_players = [Player((100,450,), "striker",side = "away"),]
		all_players = home_players +  goalies +away_players
		self.world.AddEntities([ball  ] + all_players  + goal_lines)
		self.game_manager = GameManager()

		for p in self.world.GetEntities(Player):
			p.world = self.world

		self.game_manager.Reset(random.choice(["home", "away" ]), all_players , ball, goal = False)



	def GoHome(self):
		self.running = False 
		HomeScreen().show()

	def Pause(self):
		print("paused")
	def ShowScores(self):
		scores = self.game_manager.scores
		board_pos  = 480,20
		self.window.blit(iload(images.score_board), board_pos)
		wos(f"{scores['home']}  {scores['away']}   " ,( board_pos[0] + 160 , board_pos[1] + 15) , self.window , (0,30,60) , 40)




 
	def display_widgets(self):
		self.window.fill("gray")

		ball = self.world.GetEntities(Ball)[0]
		players = self.world.GetEntities(Player)
		goal_keepers = self.world.GetEntities(GoalKeeper)
		goal_lines = self.world.GetEntities(GoalLine)

		self.window.blit(iload(images.pitch), (0, 100))
		#message, position, window, color, fontsize,
		self.ShowScores()
		for b in self.buttons:
			b.show(self.window, pygame.mouse.get_pos() , self.events)

		self.game_manager.Manage(self.world)
		self.world.show(self.window , self.events , pygame.mouse.get_pos(), self.keys)



class  HelpScreen(Screen):
	def __init__(self):
		Screen.__init__(self)

		self.buttons = [ 
	 
		SimpleButton( (0,0), self.BackHome , "BACK" , (200, 50) )


		 ]

	def BackHome(self):
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
		SimpleButton( (200,150), self.PlayGame, "START", (240, 50) ),
		SimpleButton( (200,250), self.ShowHelpMenu, "HELP" , (240, 50) ),
		SimpleButton( (200,350), self.exit, "EXIT" , (240, 50) )


		 ]




	def ShowHelpMenu(self):
		HelpScreen().show()

	def PlayGame(self):
		print("-starting a game ..")
		self.running = False 

		GameScreen().show()
		pass 

	def display_widgets(self):

		self.window.fill(pygame.Color("white")) 
		#message, position, window, color, fontsize,
		wos(" SIMPLE SOCCER " ,( 200,50) , self.window , (0,0,0) , 50 , "Lucida console")

		for b in self.buttons:
			b.show(self.window, pygame.mouse.get_pos() , self.events)
if __name__ == '__main__':
	HomeScreen().show()