from GameFrame import RoomObject,  Globals
import pygame
from Objects.enemys import Asteroid
import random
class Plane(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("plane.png")
        self.set_image(image,100,100)


        asteroid_spawn_time = random.randint(15,150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)


        # register events
        self.handle_key_events = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w] and key[pygame.K_a]:
            self.y -= 10
            self.x -= 10
        elif key[pygame.K_w] and key[pygame.K_d]:
            self.y -= 10
            self.x += 10
        elif key[pygame.K_s] and key[pygame.K_a]:
            self.y += 10
            self.x -= 10
        elif key[pygame.K_s] and key[pygame.K_d]:
            self.y += 10
            self.x += 10
        elif key[pygame.K_w]:
            self.y -= 15
        elif key[pygame.K_s]:
            self.y += 15
        elif key[pygame.K_d]:
            self.x += 15
        elif key[pygame.K_a]:
            self.x -= 15


    def keep_in_room(self):
        """
        Keeps the ship inside the room
        """
        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
        if self.x < 0:
            self.x = 0
        elif self.x + self.width> Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width

    def step(self):


        self.keep_in_room()


    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_asteroid = Asteroid(self.room, self.x, 0)
        new_asteroid.y = 0 + new_asteroid.height/2
        self.room.add_room_object(new_asteroid)
        
        # reset time for next Asteroid spawn
        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)