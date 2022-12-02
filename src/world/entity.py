
 


import pygame
 
class Entity:

    """


    THE smallest unit of an object..everything is an entity 
    """
    def __init__(self,pos  , size = (50,50)  , hitbox_color = (200,54,76) ):
        print('ENTITY POS : ',pos)
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.width = size[0]
        self.height = size[1]
        self.vel = (0,0)   # VELOCITY
        self.hitbox_color = hitbox_color 
        self.walk_count = 0
        self.images = {
        "up":[], 
        "down":[],
        "left":[],
        "right":[], 
        }
 
        self.hitbox  = pygame.Rect(self.x, self.y, self.width, self.height)
        self.MOVE_LOCK = False
        
        self.SHOW_HITBOX = True
       
    # Update the current position to _> new_pos
    def UpdatePos(self, new_pos):
        self.pos =  new_pos 
        self.x, self.y = new_pos 
        self.hitbox  = pygame.Rect(self.x, self.y, self.width, self.height)
        

    # UPDATE THE CURRENT POSITION AS PER VELOCITY
    def Update(self):
        self.MoveFreely()
        x,y = self.pos
        self.x, self.y = x,y 
        self.hitbox  = pygame.Rect(x,y, self.width, self.height)
        


    # move in the provided direction
    def Move(self, direction):
        d = direction
        px,py = self.pos 
        v =self.vel
        if d == "right":
            px += v[0]
        elif d == "left":
            px -= v[0]
        elif d == "up":
            py -= v[1]
        elif d == "down":
            py += v[1]

        self.pos = px, py
            

    # move in relation to the current velocity
    def MoveFreely(self):
        if self.MOVE_LOCK :
            return
        sx,sy = self.vel
        x,y = self.pos
        self.pos = x + sx ,  y + sy 

    # for custom entity displays
    def CustomDisplay(self , window , mouse_pos , events, keys ):
    	pass 

    # show the entity to the screen 
    def show(self, window ,events , mouse_pos , keys  ):
        self.Update()
        if self.SHOW_HITBOX:
            pygame.draw.rect(window  ,self.hitbox_color, self.hitbox ,0 )
        self.CustomDisplay(window , mouse_pos ,events , keys )

 