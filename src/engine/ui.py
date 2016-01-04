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
    
    def onTick(self, millis):
        raise NotImplementedError()
    
    def onKeyDown(self, event):
        pass
    def onKeyUp(self, event):
        pass
    def onMouseMoved(self, event):
        if not self.contains_position(event.last_position) and self.contains_position(event.position):
            self.onMouseEntered(event)
        elif self.contains_position(event.last_position) and not self.contains_position(event.position):
            self.onMouseLeft(event)
        elif self.contains_position(event.last_position) and self.contains_position(event.position):
            self.onMouseMovedInside(event)
    def onMouseButtonDown(self, event):
        if self.contains_position(event.position):
            self.mouse_down_on_element = True
            self.onMouseDown(event)
    def onMouseButtonUp(self, event):
        if self.mouse_down_on_element and self.contains_position(event.position):
            self.onClicked(event)
        self.mouse_down_on_element = False
        if self.contains_position(event.position):
            self.onMouseUp(event)
    def onMouseWheelScrolled(self, event):
        if self.contains_position(event.position):
            self.onMouseScrolled(event)
    
    def onMouseEntered(self, event):
        pass
    def onMouseLeft(self, event):
        pass
    def onMouseMovedInside(self, event):
        pass
    def onMouseDown(self, event):
        pass
    def onMouseUp(self, event):
        pass
    def onClicked(self, event):
        pass
    def onMouseScrolled(self, event):
        pass


class Button(UIElement):
    def __init__(self, screen, position, dimensions):
        super(Button, self).__init__(screen, position, dimensions)
    
    def onTick(self, millis):
        pass


class TestUIElement(UIElement):
    def __init__(self, screen, position, dimensions):
        super(TestUIElement, self).__init__(screen, position, dimensions)
        self.position = Vec2(random.randint(0, 5), random.randint(0, 5))
        self.addTile(Tile('ram', Color(255, 0, 0), Color(0, 255, 0, 100)), Vec2(0, 0))
    
    def onTick(self, millis):
        pass
    
    def onMouseEntered(self, event):
        for tile in self.tiles:
            tile[0].bg_color = Color(255, 255, 255)
    def onMouseLeft(self, event):
        for tile in self.tiles:
            tile[0].bg_color = Color(0, 255, 0, 100)