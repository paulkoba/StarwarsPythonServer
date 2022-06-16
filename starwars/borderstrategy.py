from singleton import Singleton

class BorderStrategy:
    '''Shouldn't be used directly. Use one of the subclasses instead.'''
    def execute(self, obj, map_width, map_height):
        raise NotImplementedError()


class DefaultStrategy(BorderStrategy, metaclass = Singleton):
    '''Unbounded playing field.'''
    def execute(self, obj, map_width, map_height):
        pass

class WrapStrategy(BorderStrategy, metaclass = Singleton):
    '''Map wraps around itself.'''
    def execute(self, obj, map_width, map_height):
        self.wrap_position(obj, map_width, map_height)

    def wrap_position(self, obj, map_width, map_height):
        if obj.x + obj.width / 2 > map_width:
            obj.x = -obj.width / 2
        elif obj.x - obj.width / 2 < 0:
            obj.x = map_width - obj.width / 2

        if obj.y + obj.height / 2 > map_height:
            obj.y = -obj.height / 2
        elif obj.y - obj.height / 2 < 0:
            obj.y = map_height - obj.height / 2

class BounceStrategy(BorderStrategy, metaclass = Singleton):
    '''Objects bounce on collision with map borders.'''
    def execute(self, obj, map_width, map_height):
        self.bounce_position(obj, map_width, map_height)

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


def borderStrategyFactory(strategy_name):
    if strategy_name == "default":
        return DefaultStrategy()
    elif strategy_name == "wrap":
        return WrapStrategy()
    elif strategy_name == "bounce":
        return BounceStrategy()
    else:
        raise ValueError("Unknown border strategy: " + strategy_name)