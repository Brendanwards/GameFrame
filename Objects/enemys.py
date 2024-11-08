from GameFrame import RoomObject, Globals
import random
class Enemy(RoomObject):
    """
    A class for Zorks danerous obstacles
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Asteroid object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("enemy.png")
        self.set_image(image,50,49)

        angle = random.randint(30,160)
        self.set_direction(angle, 10)
        self.register_collision_object("Ship")
    def step(self):
        """
        Determines what happens to the asteroid on each tick of the game clock
        """
     
        self.outside_of_room()

    def outside_of_room(self):
        """
        removes asteroid that have exited the room
        """
        if self.x + self.width < 0:
            print("asteroid deleted")
            self.room.delete_object(self)