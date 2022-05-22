from object_2d import Object2D

class Bullet(Object2D):
    def __init__(self, x:int, y:int, target_x:int, target_y:int, speed_multiplier:int = 5):
        super().__init__(13, 13)
        self.x = x
        self.y = y
        self.speed_multiplier = speed_multiplier
        # Normalize vector
        dist = ((target_x - x)**2 + (target_y - y)**2)**0.5
        self.velocity_x = (target_x - x) / dist * self.speed_multiplier
        self.velocity_y = (target_y - y) / dist * self.speed_multiplier

        self.name = "Bullet"

class Spaceship(Object2D):
    def __init__(self, x = 500, y = 500, id = 0):
        super().__init__(48, 48)
        self.mass = 10
        self.name = "Spaceship"
        self.x = x
        self.y = y
        self.bullets = []
        self.reload_time = 0
        self.remaining_ammo = 0
        self.id = id

    def shoot(self, target_x, target_y):
        if self.reload_time < 0.1:
            bullet = Bullet(self.x, self.y, target_x, target_y)
            self.bullets.append(bullet)
            self.remaining_ammo = 5
            self.reload_time = 1

    def update(self):
        self.reload_time -= 0.2
        if(self.reload_time < 0):
            self.reload_time = 0

        