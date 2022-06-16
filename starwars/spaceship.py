from object_2d import Object2D
import uuid
import random

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
    def __init__(self, cfg, x = 500, y = 500, id = 0, private_id = 0):
        super().__init__(cfg.safe_get('spaceship', 'spaceship_width'), cfg.safe_get('spaceship', 'spaceship_width'))
        self.mass = cfg.safe_get('spaceship', 'spaceship_mass')
        self.name = "Spaceship"
        self.x = x
        self.y = y
        self.bullets = []
        self.reload_time = 0
        self.remaining_ammo = 0
        self.id = id
        self.private_key = private_id
        self.shield_duration = 0
        self.auto_shooter_duration = 0


    def shoot(self, target_x, target_y):
        if self.reload_time < 0.1:
            bullet = Bullet(self.x, self.y, target_x, target_y)
            self.bullets.append(bullet)
            self.remaining_ammo = 5
            self.reload_time = 1

    def update(self):        
        if(self.shield_duration > 0):
            self.shield_duration -= 1

        if(self.auto_shooter_duration > 0):
            self.auto_shooter_duration -= 1
            
            bullet = Bullet(self.x, self.y, self.x + random.randint(-10, 10), self.y + random.randint(-10, 10))
            self.bullets.append(bullet)
            self.remaining_ammo = 5
            self.reload_time = 1
        
        self.reload_time -= 0.2
        if(self.reload_time < 0):
            self.reload_time = 0

    def to_dict(self):
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "spd_x": self.velocity_x,
            "spd_y": self.velocity_y,
            "bullets": [bullet.to_dict() for bullet in self.bullets],
            "reload_time": self.reload_time,
            "remaining_ammo": self.remaining_ammo,
            "id": self.id,
            "shield_duration": self.shield_duration,
        }