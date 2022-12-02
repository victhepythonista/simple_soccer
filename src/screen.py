import pygame, sys, os 



class Screen:
    '''

    a basic screen   

    HAS NO FRAME BY DEFAULT 



    '''
    def __init__(self, size = (900,500), fps = 50, title = 'basic screen', noframe = False):
        pygame.init()
        self.running = True
        self.name = ""
        self.size = size
        self.keys = []
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.events = pygame.event.get()
        pygame.display.set_caption(title) # show the tittle
        self.window = pygame.display.set_mode(self.size, pygame.NOFRAME  ) if noframe else pygame.display.set_mode(self.size  )

    # screen backend processes
    def screen_backend(self):

        self.clock.tick(self.fps)
        pygame.display.set_caption(self.name)



    def exit(self):
        # exit the screen
        self.running = False

    def quit_event(self  ):
            # anticipate a quit event
        # iterate events
        for ev in self.events:
            if ev.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                sys.exit()
    def dipslay_widgets(self):
        pass
    def show(self):

        # dispaly the contents
        while self.running:
            self.display_widgets()
            # get events
            self.events = pygame.event.get() 

            # get keys pressed
            self.keys = pygame.key.get_pressed()
            self.screen_backend()

            self.quit_event()
            pygame.display.update()
            continue
