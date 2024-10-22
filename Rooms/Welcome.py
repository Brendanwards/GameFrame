from GameFrame import Level, Globals
from Objects.title import Score, Controls

class Welcome(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.add_room_object(Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 
                           20, 
                           str(Globals.SCORE)))

        self.lives = Controls(self, Globals.SCREEN_WIDTH - 800, 400,
                               str(Globals.CONTROLS))
        self.add_room_object(self.lives)
        