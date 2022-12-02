import pygame
import random
from tools import write_on_screen


class Animation:
    ''' displays the message on to a screen for a limited period before 'dying' '''
    def  __init__(self, message, position,time_limit = 100, font_size = 20, color = (45,45,45), sound_name = ''):
        self.font_size = font_size
        self.color = color
        self.position = position
        self.timer = 0
        self.time_limit = time_limit
        self.message = message
        self.dead = False
        self.sound_name = sound_name

    # display the animation
    def show(self, window):
        self.timer += 1
        # check if time lmit is reached
        if self.timer >= self.time_limit:
            self.dead = True
        write_on_screen(self.message, self.position, window, self.color, self.font_size)
class InfoAnimation(Animation):
    '''
    for displaying basic sentence animations
    '''
    def  __init__(self, message, position,time_limit = 100, font_size = 20, color = (145,145,0)):
        Animation.__init__(self, message, position, time_limit,font_size, color)
        self.x = position[0]
        self.y = position[1]
        self.font_limits = [font_size , font_size + 100]
        self.font_countdown = 10

    def show(self, window):
        self.position = self.x,self.y
        self.timer += 1
        if self.timer >= 50:
            self.dead = True
        write_on_screen(self.message, self.position, window, self.color, self.font_size)
class PointAnimation:
    '''
    points will have an effect of floating up and dissapearing'''
    def  __init__(self, message, position,time_limit = 100, font_size = 40, color = (0,65,150)):
        Animation.__init__(self, message, position, time_limit,font_size, color)
        pos_x = int(position[0])
        self.x = random.randint(pos_x - 50, pos_x + 50)
        self.y = position[1]
        self.speed = 1
    def show(self, window):
        self.y -= self.speed
        self.timer += 1
        if self.timer >= self.time_limit:
            self.dead = True
        write_on_screen(self.message, (self.x,self.y), window, self.color, self.font_size)
 