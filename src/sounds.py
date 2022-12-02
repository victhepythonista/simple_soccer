import pygame
import time
import threading

                     
# sound files 
sounds = {
'shoot':'./data/sounds/swoosh.mp3',
'score_goal':'./data/sounds/scout_whistle_blow_2.mp3',
"ball_out":"./data/sounds/scout_whistle_blow_short.mp3"


 
}

background_music = {
	'jazz_french':'./data/sounds/jazzfrenchy.mp3',
	'hipjazz':'./data/sounds/bensound-hipjazz.mp3',
 
}

 

def load_sound(path, volume = .4):
	# return a pygame.mixer.sound object
	pygame.mixer.init()
	sound = pygame.mixer.Sound(path)
	sound.set_volume(volume)
	return  sound
# handles game s
class GameSounds:
    '''
    manages the in-game Sounds
    '''
    @staticmethod
    def load_and_play(sound,volume ):
    	pygame.mixer.init()
    	pygame.mixer.music.stop()
    	pygame.mixer.music.set_volume(volume)
    	pygame.mixer.music.load(sound )
    	pygame.mixer.music.play()
    	if pygame.mixer.music.get_busy() == False:
    		GameSounds.load_and_play(sound, volume)

    	 
    @staticmethod
    def background_music(soundname = 'jazz_french', volume = .1):
    	# continuously play background music
    	GameSounds.load_and_play(background_music[soundname],volume)
    @staticmethod
    def  UI_background_music(soundname = 'hipjazz', volume = .1):
    	GameSounds.load_and_play(background_music[soundname], volume)
    #--------------- sound objects ------------------------#
    @staticmethod
    def play(soundname, volume = 1):

    	target = GameSounds.play_sound
    	thread = threading.Thread(target = target, args = (soundname,volume))
    	thread.start()
        
    @staticmethod
    def play_sound(soundname, volume):
        pygame.mixer.init()

        sound  = load_sound(sounds[soundname])
        try:
            sound.play()
        except:
            return
    


#test_sound = 'bounce_2'
#while True:
#	GameSounds.play(test_sound)
#	time.sleep(1)

#GameSounds.play('bounce_2')

 