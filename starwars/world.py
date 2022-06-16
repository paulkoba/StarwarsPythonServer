import random
import json
from time import sleep
from asteroids import SmallAsteroid, BigAsteroid  
from spaceship import Spaceship, Bullet
from singleton import Singleton
from borderstrategy import BorderStrategy, DefaultStrategy, WrapStrategy, BounceStrategy, borderStrategyFactory
from asteroiddecorator import AsteroidDecorator

class World(metaclass = Singleton):
    def __init__(self, cfg):
        self.cfg = cfg
        self.width = cfg.safe_get("world", "width")
        self.height = cfg.safe_get("world", "height")
        self.objects = []
        self.spaceships = [] # Array of spaceship references
        self.asteroid_decorator = AsteroidDecorator(self.cfg, self.objects)
        self.generate_big_asteroids(cfg.safe_get("world", "starting_asteroids"))
        self.tick_count = 0
        self.strategy = borderStrategyFactory(cfg.safe_get("world", "border_strategy"))
        self.callbacks = []

    def subscribe(self, callback):
        self.callbacks.append(callback)

    def unsubscribe(self, callback):
        self.callbacks.remove(callback)

    def notify(self):
        for callback in self.callbacks:
            callback(self)

    def generate_big_asteroids(self, number):
        ''' This algorithm generates asteroids in random positions with random velocities. '''
        for i in range(number):
            self.objects.append(BigAsteroid(self.cfg))
            self.asteroid_decorator.decorateRandomPosition(self.objects[-1])
            self.asteroid_decorator.decorateRandomVelocity(self.objects[-1])

    def resolve_collisions(self):
        ''' This algorithm resolves collisions between objects. '''
        for i in range(len(self.objects)):
            for j in range(i+1, len(self.objects)):
                if self.objects[i].name == "Spaceship" and self.objects[j].name != "Shield" and self.objects[j].name != "AutoShooter":
                    for k in range(len(self.objects[i].bullets)):
                        if self.objects[j].check_collision(self.objects[i].bullets[k]):
                            self.objects[j].destroy(self.objects)
                            del self.objects[i].bullets[k]
                            del self.objects[j]

                elif self.objects[j].name == "Spaceship" and self.objects[j].name != "Shield" and self.objects[j].name != "AutoShooter":
                    for k in range(len(self.objects[j].bullets)):
                        if self.objects[i].check_collision(self.objects[j].bullets[k]):
                            self.objects[i].destroy(self.objects)
                            del self.objects[j].bullets[k]
                            del self.objects[i]

                elif self.objects[i].check_collision(self.objects[j]):
                    self.objects[i].collide(self.objects[j])

                    if self.objects[i].name == "Spaceship" and self.objects[j].name == "Shield":
                        self.objects[i].shield_duration += self.cfg.safe_get("spaceship", "shield_duration")

                        self.objects[j].destroy(self.objects)
                        del self.objects[j]

                    if self.objects[i].name == "Spaceship" and self.objects[j].name == "AutoShooter":
                        self.objects[i].auto_shooter_duration += self.cfg.safe_get("spaceship", "auto_shooter_duration")

                        self.objects[j].destroy(self.objects)
                        del self.objects[j]

                    if self.objects[i].name == "Spaceship" or self.objects[j].name == "Spaceship":
                        if self.objects[i].name == "Spaceship" and self.objects[i].shield_duration > 0:
                            continue
                        
                        if self.objects[j].name == "Spaceship" and self.objects[j].shield_duration > 0:
                            continue

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
            obj.move(self.width, self.height, self.strategy)

            if(obj.name == "Spaceship"):
                for bullet in obj.bullets:
                    bullet.move(self.width, self.height, self.strategy)

        self.tick_count += 1

        self.notify()

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

    def getSpaceshipByID(self, id):
        for i in range(len(self.spaceships)):
            if self.objects[self.spaceships[i]].id == id:
                return self.spaceships[i]

        return None

    def foreachObject(self, func):
        for i in range(len(self.objects)):
            func(self.objects[i])

    def foreachOfType(self, type, func):
        for i in range(len(self.objects)):
            if self.objects[i].name == type:
                func(self.objects[i])