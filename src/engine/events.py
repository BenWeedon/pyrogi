LEFT_BUTTON = 1
MIDDLE_BUTTON = 2
RIGHT_BUTTON = 3
SCROLL_WHEEL_UP = 4
SCROLL_WHEEL_DOWN = 5

class Event(object):
    pass

class KeyDownEvent(Event):
    def __init__(self, character, key, modifier):
        self.character = character
        self.key = key
        self.modifier = modifier
class KeyUpEvent(Event):
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier
class MouseMovedEvent(Event):
    def __init__(self, position, relativePosition, buttons):
        self.position = position
        self.relativePosition = relativePosition
        self.buttons = buttons
class MouseButtonDownEvent(Event):
    def __init__(self, position, button):
        self.position = position
        self.button = button
class MouseButtonUpEvent(Event):
    def __init__(self, position, button):
        self.position = position
        self.button = button
class MouseWheelScrolledEvent(Event):
    def __init__(self, position, scrollAmount):
        self.position = position
        self.scrollAmount = scrollAmount