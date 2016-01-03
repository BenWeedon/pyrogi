import random
from engine.backend import UIElementContainer
from engine.graphics import Tile, Color, Drawable
from engine.util.vector import Vec2

class UIElement(UIElementContainer):
    def __init__(self, screen, position, dimensions):
        UIElementContainer.__init__(self)
        Drawable.__init__(self)
        self.screen = screen
        self.position = position
        self.dimensions = dimensions
    
    def onTick(self, millis):
        raise NotImplementedError()

class TestUIElement(UIElement):
    def __init__(self, screen, position, dimensions):
        super(TestUIElement, self).__init__(screen, position, dimensions)
        self.position = Vec2(random.randint(0, 5), random.randint(0, 5))
        self.addTile(Tile(self.position, None, Color(255, 0, 0), Color(0, 255, 0, 100)))
    
    def onTick(self, millis):
        pass