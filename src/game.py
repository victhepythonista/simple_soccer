import pygame, time  


from buttons import UIButton 
from screen import Screen
from tools import write_on_screen as wos , iload 

from paths import images 
from world import World , Entity ,Ball 





class ScreenManager:

	def __init__(self):

		self.screens = []



class GameScreen(Screen):
	def __init__(self):
		Screen.__init__(self)

		self.score = [0,0]
		self.entities = [] 
		self.paused = False 
		self.buttons = [ 
		UIButton( (30,0), self.Pause, "PAUSE", size = (50,20) ),
		UIButton( (80,0), self.GoHome, "BACK" ,size = (50,20)),


		 ]


		self.world = World() 
		ball = Ball((200,100))
		self.world.AddEntities([ball  ,])




	def GoHome(self):
		self.running = False 
		HomeScreen().show()

	def Pause(self):
		print("paused")
	def ShowScores(self):
		s = self.score 
		wos(f"PC {s[0]} : {s[1]} YOU  " ,( 100,50) , self.window , (0,30,60) , 40)




 
	def display_widgets(self):

		self.window.blit(iload(images["home_bg"]), (0, 100))
		#message, position, window, color, fontsize,
		self.ShowScores()
		for b in self.buttons:
			b.show(self.window, pygame.mouse.get_pos() , self.events)

		self.world.show(self.window , self.events , pygame.mouse.get_pos())

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