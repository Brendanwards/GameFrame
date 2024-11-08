from GameFrame import RoomObject,  Globals
import pygame
from Objects.laser import Laser
from Objects.enemys import Enemy
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


        enemy_spawn_time = random.randint(15,150)
        self.set_timer(enemy_spawn_time, self.spawn_enemy)

        # handle events
        self.register_collision_object("Enemy")

        # register events
        self.handle_key_events = True
        self.can_shoot = True
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
        if key[pygame.K_SPACE]:
            self.shoot_laser()

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


    def spawn_enemy(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_enemy = Enemy(self.room, self.x, 0)
        new_enemy.y = 0 + new_enemy.height/2
        self.room.add_room_object(new_enemy)
        
        # reset time for next Asteroid spawn
        enemy_spawn_time = random.randint(15, 150)
        self.set_timer(enemy_spawn_time, self.spawn_enemy)

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        
        if other_type == "Ship":
            self.room.running = False


    def shoot_laser(self):
        """
        Shoots a laser from the ship
        """
        if self.can_shoot:
            new_laser = Laser(self.room, 
                            self.x + self.width/2, 
                            self.y + self.height/2 - 4)
            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            
    def reset_shot(self):
        """
        Allows ship to shoot again
        """
        self.can_shoot = True

    def handle_collision(self, other, other_type):
        """
        Handles laser collisions with other registered objects
        """
        if other_type == "Enemy":
            self.room.delete_object(other)