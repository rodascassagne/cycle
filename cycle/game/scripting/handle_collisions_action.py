import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        cycles = cast.get_actors("cycles")
        
        #cycle 2 touch cycle 1  it is True
        cycle2_head = cycles[1].get_segments()[0]
        cycle1_trail = cycles[0].get_segments()[1:]

        for segment in cycle1_trail:
            if cycle2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        # cycle 1 touch cycle 2  it is True
        cycle1_head = cycles[0].get_segments()[0]
        cycle2_trail = cycles[1].get_segments()[1:]

        for segment in cycle2_trail:
            if cycle1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

        

        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("game  over")
            message.set_position(position)
            message.set_color(constants.LIME)
            message.set_font_size(50)
            cast.add_actor("messages", message)

            for cycle in cycles:
                segments = cycle.get_segments()
                for segment in segments:
                    segment.set_color(constants.WHITE)
                cycle.set_color(constants.WHITE)