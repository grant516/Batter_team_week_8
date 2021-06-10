from game.action import Action

# TODO: Define the DrawActorsAction class here

class DrawActorsAction(Action):
    
    def __init__(self, output_service):

        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen() #clears the screen

        """for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)"""

        self._output_service.draw_actors(cast["ball"])
        self._output_service.draw_actors(cast["paddle"])
        self._output_service.draw_actors(cast["brick"])
        

        self._output_service.flush_buffer() #updates the new things on the screen

        