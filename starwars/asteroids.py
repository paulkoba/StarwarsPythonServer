from object_2d import Object2D

class Asteroid(Object2D):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

class BigAsteroid(Asteroid):
    def __init__(self):
        super().__init__(68, 60)
        self.mass = 10
        self.name = "BigAsteroid"

    def destroy(self, objects):
        a1 = SmallAsteroid()
        a1.x, a1.y = self.x - 20, self.y - 20
        a1.velocity_x, a1.velocity_y = self.velocity_x, self.velocity_y
        a2 = SmallAsteroid()
        a2.x, a2.y = self.x + 20, self.y + 20
        a2.velocity_x, a2.velocity_y = self.velocity_x, self.velocity_y
        objects.append(a1)
        objects.append(a2)

class SmallAsteroid(Asteroid):
    def __init__(self):
        super().__init__(44, 36)
        self.mass = 6
        self.name = "SmallAsteroid"