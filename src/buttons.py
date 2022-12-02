
import pygame, os 
import time


from sounds import GameSounds as GS
from tools import write_on_screen as wos

COLORS = {
'b_ntc':(250,250,250),
'b_htc':(250,250,0),
'b_ctc':(0,100,0),
}



class Widget:
    def __init__(self):
        
        pass 
    
    
    def AdjustRelativePosition(self, pos):
        if self.original_x and self.original_y:
            self.x = self.original_x + pos[0] 
            self.y = self.original_y + pos[1]
            self.pos =self.position  = pos
 
class SimpleButton(Widget):

    def __init__(self,pos, action,text, dimensions,args = None,kwargs = None,border_radius = 7,border_width = 0,normal_rectcolor = (25,95,155), highlighted_rectcolor = (0,170,70), highlighted_textcolor =(255,255,255) ,textcolor =(210,200,210), font_size= 30,font = 'consolas',highlight_scale_factor = 0):
        Widget.__init__(self)


        self.action = action # function to execuute when pressed 
        self.font = font  # text font size
        self.clicked = False
        self.args = args 
        self.kwargs = kwargs
        self.dimensions = dimensions
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.original_pos = pos 
        self.width = self.dimensions[0]
        self.height = self.dimensions[1]
        self.original_size = self.width,self.height
        self.text = text
        self.font_size = font_size
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.highlighted_rectcolor = highlighted_rectcolor
        self.normal_rectcolor = normal_rectcolor
        self.textcolor = textcolor
        self.highlighted_textcolor = highlighted_textcolor
        self.current_textcolor = self.textcolor
        self.border_radius = border_radius
        self.border_width = border_width
        self.highlighted = False
        self.rect_color = self.normal_rectcolor
        self.highlight_scale_factor = highlight_scale_factor 
        self.text_pos = self.pos
        self.SHOW_RECT = True
        self.SHOW_TEXT = True

    def Revert(self):
        # revert to the previous inactive state
        self.width,self.height = self.original_size
        self.pos = self.original_pos
        self.dimensions = self.width,self.height 
        
    def Highlighted(self):
        # highlighted, change the color accordingy
        self.current_textcolor = self.highlighted_textcolor
        self.rect_color = self.highlighted_rectcolor
        self.CustomHighlighted()
   
    def NotHighlighted(self):
        # not highlighted,....switch colors accordingly
        self.rect_color = self.normal_rectcolor
        self.current_textcolor = self.textcolor
        self.CustomNotHighlighted()
    
    def CustomHighlighted(self):
        # custom functions to do when highlighted 
        pass 
    
    def CustomNotHighlighted(self):
        # custom stuff to do when not highlighted
        pass 
    
    def show(self, window, mouse_pos, events):
        # dispay the button 
        self.mouse_interaction(pygame.mouse.get_pos(), events)
        if self.highlighted:
            self.Highlighted()
        else:
            self.NotHighlighted()
 
        self.pos = self.x,self.y
        self.dimensions = self.width,self.height
        self.text_pos = self.x + self.width*.2  , self.y + self.height*.25
        self.rect = pygame.Rect(self.pos,self.dimensions)
        self.DrawRect(window)
        self.CustomDisplay(window)
        self.WriteText(window)
    def CustomDisplay(self,window):
        pass
    def WriteText(self,window):
        # write the text on the screen
        if self.SHOW_TEXT:
            wos(self.text, self.text_pos, window, self.current_textcolor,self.font_size, font= self.font)
          
              
    def DrawRect(self,window):
        # draw the button rect
        if self.SHOW_RECT:
            pygame.draw.rect(window,self.rect_color,self.rect,self.border_width,border_radius=self.border_radius)
        
    def CustomDoAction(self):
        pass
    def DoAction(self):
        # perform the action --> function 
        GS().play("button_click")
        self.CustomDoAction()
        if self.args and self.kwargs:
            self.action(*self.args, **self.kwargs)
        elif self.args:
            self.action(*self.args)
        else:
            self.action()
            
    def Highlighted(self ):
        # action awhen highlighted
        pass
    

    
    def mouse_interaction(self, mouse_pos, events):
         
        if self.rect.collidepoint(mouse_pos): # check if interacted with the mouse
            # 
            
            self.highlighted = True
            self.Highlighted()
            self.current_textcolor = self.highlighted_textcolor
            self.rect_color = self.highlighted_rectcolor
            self.CustomHighlighted()
             
             # iterate events
            for ev in events:
                if ev.type == pygame.MOUSEBUTTONDOWN and self.clicked == False:
                    if ev.button == 1 or ev.button == 3:
                        self.clicked = True
                        self.DoAction()
                        time.sleep(.1)
                else:
                    self.clicked = False
        else:
            self.highlighted = False
            self.Revert()

  
  