import random
from engine.backend import UIElementContainer
from engine.graphics import Tile, Color, Drawable
from engine.util.vector import Vec2

class UIElement(UIElementContainer):
    def __init__(self, screen, position, dimensions):
        UIElementContainer.__init__(self, position)
        self.screen = screen
        self.dimensions = dimensions
        self.mouse_down_on_element = False
    
    def on_tick(self, millis):
        raise NotImplementedError()
    
    def on_key_down(self, event):
        pass
    def on_key_up(self, event):
        pass
    def on_mouse_moved(self, event):
        if not self.contains_position(event.last_position) and self.contains_position(event.position):
            self.on_mouse_entered(event)
        elif self.contains_position(event.last_position) and not self.contains_position(event.position):
            self.on_mouse_left(event)
        elif self.contains_position(event.last_position) and self.contains_position(event.position):
            self.on_mouse_moved_inside(event)
    def on_mouse_button_down(self, event):
        if self.contains_position(event.position):
            self.mouse_down_on_element = True
            self.on_mouse_down(event)
    def on_mouse_button_up(self, event):
        if self.mouse_down_on_element and self.contains_position(event.position):
            self.on_clicked(event)
        self.mouse_down_on_element = False
        if self.contains_position(event.position):
            self.on_mouse_up(event)
    def on_mouse_wheel_scrolled(self, event):
        if self.contains_position(event.position):
            self.on_mouse_scrolled(event)
    
    def on_mouse_entered(self, event):
        pass
    def on_mouse_left(self, event):
        pass
    def on_mouse_moved_inside(self, event):
        pass
    def on_mouse_down(self, event):
        pass
    def on_mouse_up(self, event):
        pass
    def on_clicked(self, event):
        pass
    def on_mouse_scrolled(self, event):
        pass


class Button(UIElement):
    def __init__(self, screen, position, dimensions):
        super(Button, self).__init__(screen, position, dimensions)
    
    def on_tick(self, millis):
        pass


class TestUIElement(UIElement):
    def __init__(self, screen, position, dimensions):
        super(TestUIElement, self).__init__(screen, position, dimensions)
        self.position = Vec2(random.randint(0, 5), random.randint(0, 5))
        self.add_tile(Tile('ram', Color(255, 0, 0), Color(0, 255, 0, 100)), Vec2(0, 0))
    
    def on_tick(self, millis):
        pass
    
    def on_mouse_entered(self, event):
        for tile in self.tiles:
            tile[0].bg_color = Color(255, 255, 255)
    def on_mouse_left(self, event):
        for tile in self.tiles:
            tile[0].bg_color = Color(0, 255, 0, 100)