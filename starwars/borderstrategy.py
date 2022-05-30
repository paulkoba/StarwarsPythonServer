class BorderStrategy:
    def execute(self, obj, map_width, map_height):
        raise NotImplementedError()


class DefaultStrategy(BorderStrategy):
    def execute(self, obj, map_width, map_height):
        pass

class WrapStrategy(BorderStrategy):
    def execute(self, obj, map_width, map_height):
        WrapStrategy.wrap_position(obj, map_width, map_height)

    def wrap_position(self, obj, map_width, map_height):
        if obj.x + obj.width / 2 > map_width:
            obj.x = -obj.width / 2
        elif obj.x - obj.width / 2 < 0:
            obj.x = map_width - obj.width / 2

        if obj.y + obj.height / 2 > map_height:
            obj.y = -obj.height / 2
        elif obj.y - obj.height / 2 < 0:
            obj.y = map_height - obj.height / 2

class BounceStrategy(BorderStrategy):
    def execute(self, obj, map_width, map_height):
        BounceStrategy.bounce_position(self, obj, map_width, map_height)

    def bounce_position(self, obj, map_width, map_height):
        if obj.x + obj.width / 2 > map_width:
            obj.velocity_x = -obj.velocity_x
            obj.x = map_width - obj.width / 2
        elif obj.x - obj.width / 2 < 0:
            obj.velocity_x = -obj.velocity_x
            obj.x = obj.width / 2

        if obj.y + obj.height / 2 > map_height:
            obj.velocity_y = -obj.velocity_y
            obj.y = map_height - obj.height / 2
        elif obj.y - obj.height / 2 < 0:
            obj.velocity_y = -obj.velocity_y
            obj.y = obj.height / 2