import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        #self._keys[119] = Point(0, -1) # w
        #self._keys[115] = Point(0, 1) # s
        self._keys[97] = Point(-1, 0) # a
        self._keys[100] = Point(1, 0) # d

        self._direction = Point(1, 0)
        
    def set_direction(self, direction):
        self._direction = direction


    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            elif(event.key_code == 97):
                self._direction = Point(-1, 0)
            elif(event.key_code == 100):
                self._direction = Point(1, 0)
            #self._direction = self._keys.get(event.key_code, Point(0, 0))
        return self._direction