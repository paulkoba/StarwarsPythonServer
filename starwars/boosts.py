from object_2d import Object2D

class Shield(Object2D):
    def __init__(self):
        super().__init__(63, 63)
        self.name = "Shield"

class AutoShooter(Object2D):
    def __init__(self):
        super().__init__(63, 63)
        self.name = "AutoShooter"