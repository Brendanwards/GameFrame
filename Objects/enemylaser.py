from GameFrame import RoomObject, Globals


class EnemyLaser(RoomObject):

    def __init__(self, room, x, y):
        """
        Inistialise the laser
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Laser.png")
        self.set_image(image, 9, 33)
        #
        
        # set movement
        self.set_direction(90, 20)
    

        self.register_collision_object("Plane")
    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        

    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)