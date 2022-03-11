import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color):
        super().__init__()
        self._segments = []
        self.set_color(color)
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        #move all segments
        for segment in self._segments:
            segment.move_next()
        #update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_cycle(self):
        return self._segments[0]

    def growing_cycle(self, game):
        for i in range(game):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_color(self.get_color())
            self._segments.append(segment)
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")            
            

    def turn_cycle(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = 0
        y = 0

        if (self.get_color() == constants.AQUA):
            x = int(constants.MAX_X / 4)
            y = int(constants.MAX_Y / 2)
        else:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "0" if i == 0 else "#"
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self.get_color())
            self._segments.append(segment)