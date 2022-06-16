import random
import string
from world import World
from configmanager import ConfigManager
from spaceship import Spaceship

class WorldFacade:
    def __init__(self, cfg):
        self.cfg = cfg
        self.w = World(self.cfg)

    def create_spaceship(self) -> int:
        self.world.objects.append(Spaceship(self.cfg))
        self.world.spaceships.append(self.world.objects[-1])
        self.world.objects[-1].id = random.randint(0, 10000000000000000)
        self.world.objects[-1].private_id = random.randint(0, 10000000000000000)
        self.world.objects[-1].x = random.randint(0, self.world.width)
        self.world.objects[-1].y = random.randint(0, self.world.height)

        return self.world.objects[-1].id, self.world.objects[-1].private_id

    def move_spaceship(self, dir, id, private_id):
        ship = self.world.getSpaceshipByID(id)

        if ship.private_id != private_id:
            return

        if dir == "up":
            ship.impulse_y = -1 * ship.speed_multiplier
        elif dir == "down":
            ship.impulse_y = 1 * ship.speed_multiplier
        elif dir == "left":
            ship.impulse_x = -1 * ship.speed_multiplier
        elif dir == "right":
            ship.impulse_x = 1 *ship.speed_multiplier

    def shoot(self, id, private_id, target_x, target_y):
        ship = self.world.getSpaceshipByID(id)

        if ship.private_id != private_id:
            return

        ship.shoot(target_x, target_y)

    def getSerializedState(self):
        return self.world.toJSON()

    def update(self):
        self.world.update()