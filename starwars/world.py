import random
import json
from time import sleep
from asteroids import SmallAsteroid, BigAsteroid  
from spaceship import Spaceship, Bullet

class World:
    def __init__(self):
        self.width = 1000
        self.height = 1000
        self.objects = []
        self.objects.append(Spaceship())
        self.objects[0].shoot(250, 250)
        self.generate_big_asteroids(10)
        self.tick_count = 0
        
    def generate_big_asteroids(self, number):
        ''' This algorithm generates asteroids in random positions with random velocities. '''
        for i in range(number):
            x, y = 0, 0
            while True:
                x, y = random.randint(0, self.width), random.randint(0, self.height)
                can_procceed = True

                for obj in self.objects:
                    if obj.check_collision_with_circle(x, y, obj.get_radius()):
                        can_procceed = False
                        break

                if can_procceed:
                    b = BigAsteroid()
                    b.x, b.y = x, y
                    b.velocity_x, b.velocity_y = random.random() * 10 - 5, random.random() * 10 - 5
                    self.objects.append(b)
                    break

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

    def toJSON(self):
        ''' Converts game state to JSON. '''
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)