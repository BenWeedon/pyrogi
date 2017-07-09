import math
import pyrogi
from pyrogi.util import Vec2

LEFT_BUTTON = 1
MIDDLE_BUTTON = 2
RIGHT_BUTTON = 3
SCROLL_WHEEL_UP = 4
SCROLL_WHEEL_DOWN = 5

def _pixel_position_to_tile_position(position):
    """:param position: The pixel position to convert.
    :type position: Vec2
    :returns: The given pixel position's corresponding tile position.
    :rtype: Vec2
    """
    tile_dimensions = pyrogi.get_tile_dimensions()
    return Vec2(math.floor(position.x/tile_dimensions.x), math.floor(position.y/tile_dimensions.y))

class Event(object):
    """An event, such as a key event or mouse event, handled by the
    :class:`~pyrogi.Backend`.
    """
    pass

class KeyDownEvent(Event):
    """An event triggered when a key is pressed down.

    The :code:`__init__` method is as follows:

    :param character: The character representing the key pressed.
    :type character: str
    :param key: The key pressed.
    :type key: int
    :param modifier: The modifier key pressed.
    :type modifier: int
    """
    def __init__(self, character, key, modifier):
        self.character = character
        self.key = key
        self.modifier = modifier
class KeyUpEvent(Event):
    """An event triggered when a key is released.

    The :code:`__init__` method is as follows:

    :param key: The key released.
    :type key: int
    :param modifier: The modifier key released.
    :type modifier: int
    """
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier
class MouseMovedEvent(Event):
    """An event triggered when the mouse is moved.

    The :code:`__init__` method is as follows:

    :param position: The current position of the mouse.
    :type position: tuple
    :param relative_position: The vector representing the motion of the mouse.
    :type relative_position: tuple
    :param buttons: The buttons pressed on the mouse.
    :type buttons: list
    """
    def __init__(self, position, relative_position, buttons):
        self.position = _pixel_position_to_tile_position(Vec2(position))
        self.relative_pixels = Vec2(relative_position)
        self.last_position = _pixel_position_to_tile_position(Vec2(position)-Vec2(relative_position))
        self.relative_tiles = self.position - self.last_position
        self.buttons = buttons
class MouseButtonDownEvent(Event):
    """An event triggered when a mouse button is pressed down.

    The :code:`__init__` method is as follows:

    :param position: The current position of the mouse.
    :type position: tuple
    :param button: The button pressed.
    :type button: button
    """
    def __init__(self, position, button):
        self.position = _pixel_position_to_tile_position(Vec2(position))
        self.button = button
class MouseButtonUpEvent(Event):
    """An event triggered when a mouse button is released.

    The :code:`__init__` method is as follows:

    :param position: The current position of the mouse.
    :type position: tuple
    :param button: The button released.
    :type button: button
    """
    def __init__(self, position, button):
        self.position = _pixel_position_to_tile_position(Vec2(position))
        self.button = button
class MouseWheelScrolledEvent(Event):
    """An event triggered when the mouse wheel is scrolled.

    The :code:`__init__` method is as follows:

    :param position: The current position of the mouse.
    :type position: tuple
    :param scroll_amount: The amount scrolled.
    :type scroll_amount: int
    """
    def __init__(self, position, scroll_amount):
        self.position = _pixel_position_to_tile_position(Vec2(position))
        self.scroll_amount = scroll_amount
