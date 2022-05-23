import random
import json
from time import sleep
from asteroids import SmallAsteroid, BigAsteroid  
from spaceship import Spaceship, Bullet
from singleton import Singleton
import asteroidfactory

class World(metaclass = Singleton):
    def __init__(self, cfg):
        self.cfg = cfg
        self.width = cfg.safe_get("world", "width")
        self.height = cfg.safe_get("world", "height")
        self.objects = []
        self.objects.append(Spaceship(self.cfg))
        self.objects[0].shoot(250, 250)
        self.generate_big_asteroids(cfg.safe_get("world", "starting_asteroids"))
        self.tick_count = 0
        
    def generate_big_asteroids(self, number):
        ''' This algorithm generates asteroids in random positions with random velocities. '''
        for i in range(number):
            self.objects.append(asteroidfactory.create(self.cfg, self.objects, BigAsteroid))

    def resolve_collisions(self):
        ''' This algorithm resolves collisions between objects. '''
        for i in range(len(self.objects)):
            for j in range(i+1, len(self.objects)):
                if self.objects[i].name == "Spaceship":
                    for k in range(len(self.objects[i].bullets)):
                        if self.objects[j].check_collision(self.objects[i].bullets[k]):
                            self.objects[j].destroy(self.objects)
                            del self.objects[i].bullets[k]
                            del self.objects[j]

                if self.objects[j].name == "Spaceship":
                    for k in range(len(self.objects[j].bullets)):
                        if self.objects[i].check_collision(self.objects[j].bullets[k]):
                            self.objects[i].destroy(self.objects)
                            del self.objects[j].bullets[k]
                            del self.objects[i]

                if self.objects[i].check_collision(self.objects[j]):
                    self.objects[i].collide(self.objects[j])

                    if self.objects[i].name == "Spaceship" or self.objects[j].name == "Spaceship":
                        self.objects[j].destroy(self.objects)
                        del self.objects[j]

                        self.objects[i].destroy(self.objects)
                        del self.objects[i]

    def update(self):
        ''' Advances game state by 1 frame. '''

        # Propagate updates to objects.
        for obj in self.objects:
            obj.update()

        # Resolve collisions and update object positions.
        self.resolve_collisions()
        for obj in self.objects:
            obj.move()

            if(obj.name == "Spaceship"):
                for bullet in obj.bullets:
                    bullet.move()

        self.tick_count += 1

    def to_dict(self):
        return {
            "tick_count": self.tick_count,
            "objects": [obj.to_dict() for obj in self.objects],
            "width": self.width,
            "height": self.height,
        }

    def toJSON(self):
        return json.dumps(self.to_dict(), default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
