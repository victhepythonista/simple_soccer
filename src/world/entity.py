
 

import pygame
 
class Entity:
    def __init__(self,pos  , size = (50,50) ):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.width = size[0]
        self.height = size[1]
        self.images = {
        "up":[], 
        "down":[],
        "left":[],
        "right":[], 
        }
    
        self.hitbox  = pygame.Rect(self.x, self.y, self.width, self.height)

       
 
    def Update(self):
    	x,y = self.pos
    	self.hitbox  = pygame.Rect(x,y, self.width, self.height)


    def CustomDisplay(self):
    	pass 

    def show(self, window ,events , mouse_pos ):
    	self.Update()

    	pygame.draw.rect(window  , pygame.Color("red"), self.hitbox ,0 )
    	self.CustomDisplay()

 