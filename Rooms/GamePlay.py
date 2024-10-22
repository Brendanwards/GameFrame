from GameFrame import Level
from Objects.plane import Plane
from GameFrame import Globals
class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # add objects
        self.add_room_object(Plane(self, Globals.SCREEN_WIDTH/2, 600))