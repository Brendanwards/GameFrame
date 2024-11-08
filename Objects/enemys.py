from GameFrame import RoomObject, Globals
import random
from Objects.enemylaser import EnemyLaser
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

        enemylaser_spawn_time = random.randint(15,30)
        self.set_timer(enemylaser_spawn_time, self.spawn_enemylaser)

    
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


    def spawn_enemylaser(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_enemylsaer = EnemyLaser(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_enemylsaer)
        
        # reset time for next Asteroid spawn
        EnemyLaser_spawn_time = random.randint(15, 30)
        self.set_timer(EnemyLaser_spawn_time, self.spawn_enemylaser)