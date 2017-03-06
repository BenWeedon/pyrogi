import os.path

VERSION = '0.1.2'

FONT_PATH = os.path.join('res', 'fonts')
FONT_CONFIG_EXTENSION = '.font.json'

# A global reference to the Backend currently running.
_backend = None

def get_window_dimensions():
    return _backend.window_dimensions

def get_tile_dimensions():
    return _backend.tile_dimensions

def get_caption():
    return _backend.caption

def get_mouse_position():
    return _backend.mouse_position

