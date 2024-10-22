from GameFrame import TextObject, Globals, RoomObject
import pygame


class Score(TextObject):
    """
    A class for displaying the current score
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
       
 
        """
        If the key pressed is space the game will start
        """

    def __init__(self, room, x: int, y: int, text=None):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.text = ("2025")
        self.update_text()
        
        self.handle_key_events = True 


    def key_pressed(self, key):
        """
        If the key pressed is space the game will start
        """
        
        if key[pygame.K_SPACE]:
            self.room.running = False
            
class Controls(TextObject):


    def __init__(self, room, x: int, y: int, text):
        """
        Intialises the score object
        """         
        # include attributes and methods from TextObject
        TextObject.__init__(self, room, x, y, text)
        
        # set values         
        self.size = 40
        self.font = 'Calibri'
        self.colour = (255,255,255)
        self.bold = False
        self.text = ("wasd to move and space to shoot and start")
        self.update_text()

        