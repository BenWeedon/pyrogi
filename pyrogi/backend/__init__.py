"""A package defining all the backend (i.e. non-graphical) work of the engine.
Thus, most of the implementation of the engine is underneath the
:mod:`backend` package.

The most important class exposed by the backend package is :class:`Backend`.
This class is central to the functioning of the entire pyrogi backend.
"""
import pyrogi
from pyrogi.graphics import Tile, Color, Drawable
from pyrogi.util.vector import Vec2

class Backend(object):
    """The :class:`Backend` class is intended to be extended (for example, by
    :class:`PyGameBackend`).  :class:`Backend` forwards events such as key
    events and ticks on to the current :class:`Screen`. Its implementations are
    expected to implement the :meth:`run` method, however, which should start
    up the main loop for the backend.

    The :code:`__init__` method of a :class:`Backend` is as follows:

    :param window_dimensions: The dimensions, in terms of of tiles, for the
        game window to be.
    :type window_dimensions: Vec2
    :param tile_dimensions: The dimensions, in terms of pixels, for each tile
        to be.
    :type tile_dimensions: Vec2
    :param caption: The title text of the game window.
    :type caption: str
    :param starting_screen: The screen to begin the game on.
    :type starting_screen: Screen
    """

    def __init__(self, window_dimensions, tile_dimensions, caption, starting_screen):
        pyrogi.window_dimensions = window_dimensions
        pyrogi.tile_dimensions = tile_dimensions
        self.caption = caption
        self.screens = [starting_screen]

    def run(self):
        """Run the main loop for pyrogi.

        This must be implemented by subclasses of :class:`Backend`.
        """
        raise NotImplementedError()

    def on_tick(self, millis):
        """Called by the :class:`Backend` implementation when a tick should
        occur in the game loop. This should never be overriden, but can be
        extended if the :class:`Backend` implementation wishes to do something
        every tick. The tick is passed on to the backend's current screen.

        :param millis: The number of milliseconds since the last tick.
        :type millis: int
        """
        self.get_current_screen().on_tick(millis)
    def on_draw(self, g):
        """Called by the :class:`Backend` implementation when a draw should
        occur in the game loop. This should never be overriden, but can be
        extended if the :class:`Backend` implementation wishes to do something
        every draw. The draw is passed on to the backend's current screen.

        :param g: The :class:`Graphics` object to be used to perform the
            drawing.
        :type g: Graphics
        """
        self.get_current_screen().on_draw(g)

    def get_current_screen(self):
        """:returns: The screen currently set in the engine.
        :rtype: Screen
        """
        return self.screens[-1]
    def set_screen(self, screen):
        """Sets the current screen in the engine. It is added to a stack of
        other screens, which maintains history and allows the engine to return
        to previous screens.

        :param screen: The screen to be added to the stack.
        :type screen: Screen
        """
        self.screens.append(screen)
    def go_back_n_screens(self, n):
        """Return to the nth screen in the stack, popping off screens as you
        go. Because screens are removed from the stack to reach the nth most
        recent screen, they cannot be returned to without constructing new
        ones.

        :param n: The number of screens to go back.
        :type n: int
        """
        for i in range(n):
            self.screens.pop()

    def handle_key_down(self, event):
        """Called by the :class:`Backend` implementation when a key down event
        has occured. This should never be overriden, but can be extended if the
        :class:`Backend` implementation wishes to do something every time the
        event is triggered. The event is passed on to the backend's current
        screen.

        :param event: The event triggered.
        :type event: KeyDownEvent
        """
        self.get_current_screen().handle_key_down(event)
    def handle_key_up(self, event):
        """Called by the :class:`Backend` implementation when a key up event
        has occured. This should never be overriden, but can be extended if the
        :class:`Backend` implementation wishes to do something every time the
        event is triggered. The event is passed on to the backend's current
        screen.

        :param event: The event triggered.
        :type event: KeyUpEvent
        """
        self.get_current_screen().handle_key_up(event)
    def handle_mouse_moved(self, event):
        """Called by the :class:`Backend` implementation when a mouse moved
        event has occured. This should never be overriden, but can be extended
        if the :class:`Backend` implementation wishes to do something every
        time the event is triggered. The event is passed on to the backend's
        current screen.

        :param event: The event triggered.
        :type event: MouseMovedEvent
        """
        pyrogi.mouse_position = event.position
        self.get_current_screen().handle_mouse_moved(event)
    def handle_mouse_button_down(self, event):
        """Called by the :class:`Backend` implementation when a mouse button
        down event has occured. This should never be overriden, but can be
        extended if the :class:`Backend` implementation wishes to do something
        every time the event is triggered. The event is passed on to the
        backend's current screen.

        :param event: The event triggered.
        :type event: MouseButtonDownEvent
        """
        self.get_current_screen().handle_mouse_button_down(event)
    def handle_mouse_button_up(self, event):
        """Called by the :class:`Backend` implementation when a mouse button up
        event has occured. This should never be overriden, but can be extended
        if the :class:`Backend` implementation wishes to do something every
        time the event is triggered. The event is passed on to the backend's
        current screen.

        :param event: The event triggered.
        :type event: MouseButtonUpEvent
        """
        self.get_current_screen().handle_mouse_button_up(event)
    def handle_mouse_wheel_scrolled(self, event):
        """Called by the :class:`Backend` implementation when a mouse wheel
        scrolled has occured. This should never be overriden, but can be
        extended if the :class:`Backend` implementation wishes to do something
        every time the event is triggered. The event is passed on to the
        backend's current screen.

        :param event: The event triggered.
        :type event: MouseWheelScrolledEvent
        """
        self.get_current_screen().handle_mouse_wheel_scrolled(event)


class UIElementContainer(Drawable):
    """The :class:`UIElementContainer` class defines a :class:`Drawable` which
    can contain any number of :class:`UIElement` children. This class then
    passes events, such as ticks, draws, and mouse events, on to all of the
    children.

    The :code:`__init__` method of a :class:`UIElementContainer` is as follows:

    :param position: The position in tile space of the
        :class:`UIElementContainer`.
    :type position: Vec2
    """

    def __init__(self, position):
        super(UIElementContainer, self).__init__(position)
        self.ui_elements = []

    def on_tick(self, millis):
        """Called by this object's container when a tick occurs. This should
        never be overriden, but can be extended if the
        :class:`UIElementContainer` subclass wishes to do something every tick.
        The tick event is passed on to every child of this object, in addition
        to the object's own tick method.
        # TODO actually implement this last part.

        :param millis: The number of milliseconds since the last tick.
        :type millis: int
        """
        for elt in self.ui_elements[:]:
            elt.on_tick(millis)
            elt.update_drawable(millis)
    def on_draw(self, g):
        """Called by this object's container when a draw occurs. This should
        never be overriden, but can be extended if the
        :class:`UIElementContainer` subclass wishes to do something every draw.
        The draw event is passed on to every child of this object, in addition
        to the object's own draw method.

        :param g: The :class:`Graphics` object to be used to perform the
            drawing.
        :type g: Graphics
        """
        self.draw(g)
        for elt in self.ui_elements[:]:
            elt.on_draw(g)

    def add_child(self, child):
        """Add a new child to this object's child list.

        :param child: The child to add.
        :type child: UIElementContainer
        """
        self.ui_elements.append(child)
    def remove_child(self, child):
        """Remove the given child from this object's child list.

        :param child: The child to remove.
        :type child: UIElementContainer
        """
        self.ui_elements.remove(child)

    def handle_key_down(self, event):
        """Called by this object's container when a key down event occurs. This
        should never be overriden, but can be extended if the
        :class:`UIElementContainer` subclass wishes to do something every time
        the event is triggered.  The event is passed on to every child of this
        object, in addition to the object's own on_key_down method.

        :param event: The event triggered.
        :type event: KeyDownEvent
        """
        self.on_key_down(event)
        for elt in self.ui_elements[:]:
            elt.handle_key_down(event)
    def handle_key_up(self, event):
        """Called by this object's container when a key up event occurs. This
        should never be overriden, but can be extended if the
        :class:`UIElementContainer` subclass wishes to do something every time
        the event is triggered.  The event is passed on to every child of this
        object, in addition to the object's own on_key_up method.

        :param event: The event triggered.
        :type event: KeyUpEvent
        """
        self.on_key_up(event)
        for elt in self.ui_elements[:]:
            elt.handle_key_up(event)
    def handle_mouse_moved(self, event):
        """Called by this object's container when a mouse moved event occurs.
        This should never be overriden, but can be extended if the
        :class:`UIElementContainer` subclass wishes to do something every time
        the event is triggered.  The event is passed on to every child of this
        object, in addition to the object's own on_mouse_moved method.

        :param event: The event triggered.
        :type event: MouseMovedEvent
        """
        self.on_mouse_moved(event)
        for elt in self.ui_elements[:]:
            elt.handle_mouse_moved(event)
    def handle_mouse_button_down(self, event):
        """Called by this object's container when a mouse button down event
        occurs.  This should never be overriden, but can be extended if the
        :class:`UIElementContainer` subclass wishes to do something every time
        the event is triggered.  The event is passed on to every child of this
        object, in addition to the object's own on_mouse_button_down method.

        :param event: The event triggered.
        :type event: MouseButtonDownEvent
        """
        self.on_mouse_button_down(event)
        for elt in self.ui_elements[:]:
            elt.handle_mouse_button_down(event)
    def handle_mouse_button_up(self, event):
        """Called by this object's container when a mouse button up event
        occurs.  This should never be overriden, but can be extended if the
        :class:`UIElementContainer` subclass wishes to do something every time
        the event is triggered.  The event is passed on to every child of this
        object, in addition to the object's own on_mouse_button_up method.

        :param event: The event triggered.
        :type event: MouseButtonUpEvent
        """
        self.on_mouse_button_up(event)
        for elt in self.ui_elements[:]:
            elt.handle_mouse_button_up(event)
    def handle_mouse_wheel_scrolled(self, event):
        """Called by this object's container when a mouse wheel scrolled event
        occurs.  This should never be overriden, but can be extended if the
        :class:`UIElementContainer` subclass wishes to do something every time
        the event is triggered.  The event is passed on to every child of this
        object, in addition to the object's own on_mouse_wheel_scrolled method.

        :param event: The event triggered.
        :type event: MouseWheelScrolledEvent
        """
        self.on_mouse_wheel_scrolled(event)
        for elt in self.ui_elements[:]:
            elt.handle_mouse_wheel_scrolled(event)

    def on_key_down(self, event):
        """A callback called by handle_key_down when a KeyDownEvent occurs.
        This method should be implemented by any subclass of
        :class:`UIElementContainer` which wants to act on this event.

        :param event: The event triggerd.
        :type event: KeyDownEvent
        """
        pass
    def on_key_up(self, event):
        """A callback called by handle_key_up when a KeyUpEvent occurs.
        This method should be implemented by any subclass of
        :class:`UIElementContainer` which wants to act on this event.

        :param event: The event triggerd.
        :type event: KeyUpEvent
        """
        pass
    def on_mouse_moved(self, event):
        """A callback called by handle_mouse_moved when a MouseMovedEvent
        occurs.  This method should be implemented by any subclass of
        :class:`UIElementContainer` which wants to act on this event.

        :param event: The event triggerd.
        :type event: MouseMovedEvent
        """
        pass
    def on_mouse_button_down(self, event):
        """A callback called by handle_mouse_button_down when a
        MouseButtonDownEvent occurs.  This method should be implemented by any
        subclass of :class:`UIElementContainer` which wants to act on this
        event.

        :param event: The event triggerd.
        :type event: MouseButtonDownEvent
        """
        pass
    def on_mouse_button_up(self, event):
        """A callback called by handle_mouse_button_up when a
        MouseButtonUpEvent occurs.  This method should be implemented by any
        subclass of :class:`UIElementContainer` which wants to act on this
        event.

        :param event: The event triggerd.
        :type event: MouseButtonUpEvent
        """
        pass
    def on_mouse_wheel_scrolled(self, event):
        """A callback called by handle_mouse_wheel_scrolled when a
        MouseWheelScrolledEvent occurs.  This method should be implemented by
        any subclass of :class:`UIElementContainer` which wants to act on this
        event.

        :param event: The event triggerd.
        :type event: MouseWheelScrolledEvent
        """
        pass


class Screen(UIElementContainer):
    """The :class:`Screen` class is the top level :class:`UIElementContainer`.
    It represents a single screen in a game. An example may be the menu screen,
    the main game screen, or the shop screen if you are placed in a view
    separate from the game world to shop. Because they are the top level
    container, a screen's position is always (0, 0), and its dimensions is
    always equal to that of the game window. A stack of screens is maintained
    in the :class:`Backend` object.
    """
    def __init__(self):
        super(Screen, self).__init__(Vec2(0, 0))

