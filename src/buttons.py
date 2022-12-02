
import pygame, os 
from tools import write_on_screen as wos
import time

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

class TransparentNoRectButton:
    '''
    A transparent button with no rect
    '''
    def __init__(self,pos, action,text, dimensions, normal_textcolor, highlighted_textcolor, clicked_textcolor ,  font= 30,border = 5, border_radius = 10,showrect = False):
        self.action = action
        self.clicked = False
        self.dimensions = dimensions
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.width = self.dimensions[0]
        self.height = self.dimensions[1]

        self.text = text
        self.font = font
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.highlighted_textcolor = highlighted_textcolor
        self.clicked_textcolor = clicked_textcolor
        self.normal_textcolor = normal_textcolor
        self.current_textcolor = self.normal_textcolor




        self.border = border
        self.border_radius = border_radius
        self.highlighted = False
        self.showrect = showrect
    def show(self, window, mouse_pos, events):
        text_pos = self.x  , self.y + self.height*.25
        self.rect = pygame.Rect(self.pos,self.dimensions)
        wos(self.text, text_pos, window, self.current_textcolor,self.font)
        self.mouse_interaction(mouse_pos, events)

    def transform(self, textcolor ):
        # change color depending on state
        self.current_textcolor = textcolor


    def mouse_interaction(self, mouse_pos, events):
        imaginary_rect =  pygame.Rect(mouse_pos[0], mouse_pos[1], 10,10 )
        # mouse hover
        if imaginary_rect.colliderect(self.rect):
            self.highlighted = True
            self.transform(self.highlighted_textcolor)
            for ev in events:
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.button == 1 or ev.button == 3:
                        self.transform(self.clicked_textcolor )
                        self.clicked = True
                        self.action()
                else:
                    self.clicked = False
        # no mouse interaction, normal
        else:
            self.transform(self.normal_textcolor )
            self.highlighted = False

class UIButton(TransparentNoRectButton):
    def __init__(self,pos, action,text ,size = (300,70), font= 15 ):
        TransparentNoRectButton.__init__(self, pos,action, text, size,COLORS['b_ntc'], COLORS['b_htc'], COLORS['b_ctc'], font = font)



 
class SimpleButton(Widget):

    def __init__(self,pos, action,text, dimensions,args = None,kwargs = None,border_radius = 5,border_width = 0,normal_rectcolor = (25,55,155), highlighted_rectcolor = (0,0,0), highlighted_textcolor =(255,255,255) ,textcolor =(210,200,210), font_size= 30,font = 'consolas',highlight_scale_factor = 0):
        Widget.__init__(self)
        self.action = action
        self.font = font
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
        self.current_textcolor = self.highlighted_textcolor
        self.rect_color = self.highlighted_rectcolor
        self.CustomHighlighted()
   
    def NotHighlighted(self):
        self.rect_color = self.normal_rectcolor
        self.current_textcolor = self.textcolor
        self.CustomNotHighlighted()
    
    def CustomHighlighted(self):
        # custom functions to do when highlighted 
        pass 
    
    def CustomNotHighlighted(self):
        # custm stuff to do when not highlighted
        pass 
    
    def show(self, window, mouse_pos, events):
        
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
        if self.SHOW_TEXT:
            wos(self.text, self.text_pos, window, self.current_textcolor,self.font_size, font= self.font)
          
              
    def DrawRect(self,window):
        if self.SHOW_RECT:
            pygame.draw.rect(window,self.rect_color,self.rect,self.border_width,border_radius=self.border_radius)
        
    def CustomDoAction(self):
        pass
    def DoAction(self):
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
         
        if self.rect.collidepoint(mouse_pos):
            
            self.highlighted = True
            self.Highlighted()
            self.current_textcolor = self.highlighted_textcolor
            self.rect_color = self.highlighted_rectcolor
            self.CustomHighlighted()
             
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

  
 
 
class SimpleImageButton(SimpleButton):
    def __init__(self, pos,action,dimensions,image = None,args = None,kwargs = None,border_width = 3,border_radius = 5):
        SimpleButton.__init__(self, pos, action, text = "", dimensions = dimensions ,args=args,kwargs=kwargs,border_radius=border_radius,border_width = border_width)
        self.image = image # re loaded image 
        self.original_image = image
        self.highlight_scale_factor = .2
         
        
        self.normal_rectcolor = (23,45,77)
        
    def CustomHighlighted(self):
        x,y = self.original_pos
        f  = self.highlight_scale_factor
        new_x = x - x* f
        new_y = y - y* f
        w,h = self.original_size
        new_size = w*f,h*f
        
        self.dimensions = new_size
        if self.image:
            self.image = pygame.transform.scale(self.original_image, 1+ f)
        
    def CustomNotHighlighted(self):
        self.pos = self.original_pos
        self.dimensions = self.original_size
        if self.image:
            self.image = original_image
            self.pos = self.original_pos
    def CustomDisplay(self,window):
        if self.image:
            window.blit(self.image,self.pos )
       
        
         
        
        
        
        
    
        