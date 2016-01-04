import random
from engine.backend import UIElementContainer
from engine.graphics import Tile, Color, Drawable
from engine.util.vector import Vec2

class UIElement(UIElementContainer):
    def __init__(self, screen, position, dimensions):
        UIElementContainer.__init__(self, position)
        self.screen = screen
        self.dimensions = dimensions
    
    def onTick(self, millis):
        raise NotImplementedError()


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
    
    def onMouseButtonDown(self, event):
        for tile in self.tiles:
            tile[0].bg_color = Color(255, 255, 255)
    def onMouseButtonUp(self, event):
        for tile in self.tiles:
            tile[0].bg_color = Color(0, 255, 0, 100)