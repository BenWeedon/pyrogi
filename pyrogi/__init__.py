"""The top level package for the pyrogi engine. This package defines the
components of the engine which will be included in every game, such as events,
and the classes :class:`Backend` and :class:`Screen`.
"""

import os.path

VERSION = '0.1.3'

FONT_PATH = os.path.join('res', 'fonts')
FONT_CONFIG_EXTENSION = '.font.json'

# A global reference to the Backend currently running.
_backend = None

def get_window_dimensions():
    """:returns: The dimensions in tiles of the game window.
    :rtype: Vec2
    """
    return _backend.window_dimensions

def get_tile_dimensions():
    """:returns: The dimensions in pixels of each game tile.
    :rtype: Vec2
    """
    return _backend.tile_dimensions

def get_caption():
    """:returns: The title caption of the game window.
    :rtype: str
    """
    return _backend.caption

def get_mouse_position():
    """:returns: The current position in tiles of the mouse.
    :rtype: Vec2
    """
    return _backend.mouse_position

# Expose all the root package's public members.
import pyrogi.drawing
import pyrogi.ui
import pyrogi.util

from .core import Backend, Screen
from .events import LEFT_BUTTON, MIDDLE_BUTTON, RIGHT_BUTTON, SCROLL_WHEEL_UP, SCROLL_WHEEL_DOWN
from .events import Event, KeyDownEvent, KeyUpEvent, MouseMovedEvent, MouseButtonDownEvent, MouseButtonUpEvent, MouseWheelScrolledEvent
