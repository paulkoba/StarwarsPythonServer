from borderstrategy import BorderStrategy, WrapStrategy, BounceStrategy, DefaultStrategy

class Object2D:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed_multiplier = 2
        self.impulse_x = 0
        self.impulse_y = 0
        self.mass = 1
        self.name = "Object2D"
        self.max_speed = 5

    def truncate_speed(self):
        if(abs(self.velocity_x) > self.max_speed):
            self.velocity_x = self.max_speed if self.velocity_x > 0 else -self.max_speed
        if(abs(self.velocity_y) > self.max_speed):
            self.velocity_y = self.max_speed if self.velocity_y > 0 else -self.max_speed
    
    def get_center(self):
        return self.x + self.width/2, self.y + self.height/2

    def get_radius(self):
        return (self.height + self.width) / 4

    def get_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def get_distance_from_point(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5

    def check_collision(self, other):
        return self.get_radius() + other.get_radius() > self.get_distance(other)

    def check_collision_with_circle(self, x, y, radius):
        return self.get_radius() + radius > self.get_distance_from_point(x, y)

    def collide(self, other):
        ''' Calculates new velocities after collision. '''
        dist = self.get_distance(other)
        if(dist == 0):
            return

        nx = (self.get_center()[0] - other.get_center()[0]) / dist
        ny = (self.get_center()[1] - other.get_center()[1]) / dist

        v1 = (self.velocity_x * (self.mass - other.mass) + 2 * other.mass * other.velocity_x) / (self.mass + other.mass)
        v2 = (other.velocity_x * (other.mass - self.mass) + 2 * self.mass * self.velocity_x) / (self.mass + other.mass)
        v3 = (self.velocity_y * (self.mass - other.mass) + 2 * other.mass * other.velocity_y) / (self.mass + other.mass)
        v4 = (other.velocity_y * (other.mass - self.mass) + 2 * self.mass * self.velocity_y) / (self.mass + other.mass)

        self.velocity_x, self.velocity_y = v1, v3
        other.velocity_x, other.velocity_y = v2, v4

        self.truncate_speed()
        other.truncate_speed()

    def move(self, map_width = 1000, map_height = 1000, border_strategy = BounceStrategy()):
        ''' Moves object by 1 frame without taking collisions into account. '''
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.x += self.impulse_x
        self.y += self.impulse_y

        self.impulse_x /= 1.05
        self.impulse_y /= 1.05

        if(abs(self.impulse_x) < 0.01):
            self.impulse_x = 0
        
        if(abs(self.impulse_y) < 0.01):
            self.impulse_y = 0

        border_strategy.execute(self, map_width, map_height)

        

    def destroy(self, objects):
        print("Destroyed " + self.name + " at " + str(self.x) + ", " + str(self.y))

    def update(self):
        pass

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "spd_x": self.velocity_x,
            "spd_y": self.velocity_y,
            "name": self.name
        }