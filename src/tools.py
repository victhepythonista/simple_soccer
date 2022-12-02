# USEFUL TRIGONOMETRIC , ANALYTICAL and  SCREEN UTILS functions

import pygame, math 

from math import atan2,degrees


# get the opposite side
OppositeSide = lambda side: "home" if side == "away" else "away"


# write a text onto a window
def write_on_screen(  message, position, window, color, fontsize, font = 'consolas'):
    #### _this function  writes  a message to the user
    pygame.font.init()
    try:
        mess_obj = pygame.font.SysFont(font, fontsize)
    except:
        print('no such font as %s'%font, '...')
        mess_obj = pygame.font.SysFont('consolas', fontsize)
    mess_render = mess_obj.render(message, 20, color)
    window.blit(mess_render, position)


# load an image file
def iload(path):
	return pygame.image.load(path)


# GET THE DISTANCE BETWEEN TWO 2D POINTS
def DistanceBetween(p1, p2):
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    return distance
 
# GET THE ANGLE BETWEEN TWO POINTS
def GetAngleBetween(pA, pB):
  changeInX = pB[0] - pA[0]
  changeInY = pB[1] - pA[1]
  return degrees(atan2(changeInY,changeInX))  

 
 