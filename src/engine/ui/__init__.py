import random
from engine.backend import UIElementContainer
from engine.graphics import Tile, Color
from engine.util.vector import Vec2

class UIElement(UIElementContainer):
    def __init__(self, screen, position, dimensions):
        self.screen = screen
        self.position = position
        self.dimensions = dimensions
    
    def onTick(self, millis):
        raise NotImplementedError()
    
    def onDraw(self, g):
        raise NotImplementedError()

class TestUIElement(UIElement):
    def __init__(self):
        self.position = Vec2(random.randint(0, 5), random.randint(0, 5))
    def onTick(self, millis):
        pass
    
    def onDraw(self, g):
        Tile(self.position, None, Color(255, 0, 0), Color(0, 255, 0, 100)).draw(g)