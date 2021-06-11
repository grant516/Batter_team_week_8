from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.

    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its
        velocity. Will wrap the position from one side of the screen to the
        other when it reaches the edge in either direction.

        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        actor.set_position(position)

        #Trying to find a way to disable objects from wrapping around the viewport
        # screen size (found in constants)
        # MAX_X = 80
        # MAX_Y = 20
        if x1 + x2 >= 0 and y1 + y2 + 20 <= 80: ##### <----- might need to swap x and y vice versa
            y1 += y2

        # This way of doing it might need to go in the collision class???
        # trying to find the edge of the screen with the actor (ball and/or paddle) and have it
        # switch directions on contact. This doesn't really work with the paddle though because it
        # only needs to move from left to right.
        if actor.x1 + actor.MAX_X > screen.MAX_X or actor.x1 < 0:  ###<-----what variable could we use for the "screen"
            actor.x1 = actor.x2 * -1
        if actor.y1 + actor.MAX_X > screen.MAX_Y or actor.y1 < 0:
            actor.y2 = actor.y2 * -1
