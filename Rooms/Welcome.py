from GameFrame import Level
from GameFrame import TextObject, Globals

class Welcome(Level):

    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

class Title(TextObject):
    
    def __init__(self, room, x: int, y: int, text=None):
       
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()