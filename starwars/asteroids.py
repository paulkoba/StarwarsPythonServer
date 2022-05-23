from object_2d import Object2D

class Asteroid(Object2D):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

class BigAsteroid(Asteroid):
    def __init__(self, cfg):
        super().__init__(cfg.safe_get('asteroids', 'big_asteroid_width'), cfg.safe_get('asteroids', 'big_asteroid_height'))
        self.mass = cfg.safe_get('asteroids', 'big_asteroid_mass')
        self.name = "BigAsteroid"
        self.cfg = cfg

    def destroy(self, objects):
        a1 = SmallAsteroid(self.cfg)
        a1.x, a1.y = self.x - 30, self.y - 30
        a1.velocity_x, a1.velocity_y = self.velocity_x, self.velocity_y
        a2 = SmallAsteroid(self.cfg)
        a2.x, a2.y = self.x + 30, self.y + 30
        a2.velocity_x, a2.velocity_y = self.velocity_x, self.velocity_y
        objects.append(a1)
        objects.append(a2)

class SmallAsteroid(Asteroid):
    def __init__(self, cfg):
        super().__init__(cfg.safe_get('asteroids', 'small_asteroid_width'), cfg.safe_get('asteroids', 'small_asteroid_height'))
        self.mass = cfg.safe_get('asteroids', 'small_asteroid_mass')
        self.name = "SmallAsteroid"