import random

class AsteroidDecorator:
    def __init__(self, cfg, objects):
        self.cfg = cfg
        self.objects = objects

    def decorateRandomPosition(self, b):
        ''' Creates an asteroid of a given type such that it does not collide with any other asteroids. '''
        x, y = 0, 0
        width, height = self.cfg.safe_get('world', 'width'), self.cfg.safe_get('world', 'height')
        while True:
            x, y = random.randint(0, width), random.randint(0, height)
            can_procceed = True

            for obj in self.objects:
                if obj.check_collision_with_circle(x, y, obj.get_radius()):
                    can_procceed = False
                    break

            if can_procceed:
                b.x, b.y = x, y
                break

    def decorateRandomVelocity(self, b):
        b.velocity_x, b.velocity_y = random.random() * 10 - 5, random.random() * 10 - 5