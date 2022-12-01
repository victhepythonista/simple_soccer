import pygame, math 

from math import atan2,degrees

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



def iload(path):
	return pygame.image.load(path)



 

def GetAngleBetween(pA, pB):
  changeInX = pB[0] - pA[0]
  changeInY = pB[1] - pA[1]
  return degrees(atan2(changeInY,changeInX))  

def GetPointOnCirc(angle , center , radius):
    r = radius
    cx,cy = center 
    x =  math.cos(angle)*r   
    y = math.sin(angle)*r  

    return x,y 


 

if __name__ == '__main__':


    print(GetPointOnCirc(90 , (1,1) , 3))

