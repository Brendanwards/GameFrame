from GameFrame import Level
from Objects.plane import Plane
from GameFrame import Globals
from Objects.hud import Score
class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # add objects
        self.add_room_object(Plane(self, Globals.SCREEN_WIDTH/2, 600))

        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/9 - 20, 28, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)

    def update_score(self, change):
        """
        Updates the score and redraws the text
        """
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()