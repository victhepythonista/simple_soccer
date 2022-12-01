import pygame, time  , math 


from buttons import UIButton 
from screen import Screen
from tools import write_on_screen as wos , iload 
from animation import PointAnimation
from paths import images 
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
		UIButton( (30,0), self.Pause, "PAUSE", size = (50,20) ),
		UIButton( (80,0), self.GoHome, "BACK" ,size = (50,20)),


		 ]
		self.world = World() 
		goal_lines = [GoalLine((-10, 250),"home") , GoalLine((890,250), "away")]
		ball = Ball((200,100))

		home_players = [Player((100,200,), "striker", side = "home"),GoalKeeper(goal_lines[0])]
		away_players = [Player((100,450,), "striker",side = "away"),GoalKeeper(goal_lines[1])]

		self.world.AddEntities([ball  ] + away_players +home_players  + goal_lines)
		self.game_manager = GameManager()

		for p in self.world.GetEntities(Player):
			p.world = self.world





	def GoHome(self):
		self.running = False 
		HomeScreen().show()

	def Pause(self):
		print("paused")
	def ShowScores(self):
		scores = self.game_manager.scores
		wos(f"{scores['home']} |  {scores['away']}   " ,( 100,50) , self.window , (0,30,60) , 40)




 
	def display_widgets(self):
		self.window.fill((77,115,20))

		ball = self.world.GetEntities(Ball)[0]
		players = self.world.GetEntities(Player)
		goal_lines = self.world.GetEntities(GoalLine)

		self.window.blit(iload(images["pitch"]), (0, 100))
		#message, position, window, color, fontsize,
		self.ShowScores()
		for b in self.buttons:
			b.show(self.window, pygame.mouse.get_pos() , self.events)

		self.game_manager.Manage(ball , players ,goal_lines )
		self.world.show(self.window , self.events , pygame.mouse.get_pos(), self.keys)



# home screen 
class HomeScreen(Screen):
	def __init__(self):
		Screen.__init__(self)

		self.buttons = [ 
		UIButton( (200,150), self.PlayGame, "START" ),
		UIButton( (200,250), self.exit, "EXIT" )

		 ]




	def PlayGame(self):
		print("-starting a game ..")
		self.running = False 

		GameScreen().show()
		pass 

	def display_widgets(self):

		self.window.fill(pygame.Color("cyan")) 
		#message, position, window, color, fontsize,
		wos("SOCCER GAME " ,( 100,50) , self.window , (0,0,0) , 40)

		for b in self.buttons:
			b.show(self.window, pygame.mouse.get_pos() , self.events)
if __name__ == '__main__':
	GameScreen().show()