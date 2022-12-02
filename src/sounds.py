### this script handles all  sound playing  mechanisms
##########




import pygame
import time
import threading

                     
# sound files 
sounds = {
'shoot':'./data/sounds/swoosh1.mp3',
'score_goal':'./data/sounds/scout_whistle_blow_2.mp3',
"ball_out":"./data/sounds/scout_whistle_blow_short.mp3",
"deflect":"./data/sounds/deflect2.mp3",
"button_click":"./data/sounds/button_click.mp3"


 }
 

def load_sound(path, volume = .4):
	# return a pygame.mixer.sound object
	pygame.mixer.init()
	sound = pygame.mixer.Sound(path)
	sound.set_volume(volume)
	return  sound

 
class GameSounds:
    '''
    manages the in-game Sounds

    refers the sounds DICT  to get the sounds
    '''

    #  load the sound and play
    @staticmethod
    def load_and_play(sound,volume ):
    	pygame.mixer.init()
    	pygame.mixer.music.stop()
    	pygame.mixer.music.set_volume(volume)
    	pygame.mixer.music.load(sound )
    	pygame.mixer.music.play()
    	if pygame.mixer.music.get_busy() == False:
    		GameSounds.load_and_play(sound, volume)

    # play a sound using  its key in the sounds dict
    @staticmethod
    def play(soundname, volume = 1):

        # start a new thread  play the sound
    	target = GameSounds.play_sound

    	thread = threading.Thread(target = target, args = (soundname,volume))
    	thread.start()
        
    # play a sound
    @staticmethod
    def play_sound(soundname, volume):
        pygame.mixer.init()

        sound  = load_sound(sounds[soundname])
        sound.play()
    

 