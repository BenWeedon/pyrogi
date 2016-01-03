from engine.graphics import Tile, Color, Drawable
from engine.util.vector import Vec2

class Backend(object):
    def __init__(self, game, window_dimensions, tile_dimensions, caption):
        self.game = game
        self.window_dimensions = window_dimensions
        self.tile_dimensions = tile_dimensions
        self.caption = caption
    
    def run(self):
        raise NotImplementedError()


class Game(object):
    def __init__(self, starting_screen):
        self.screens = [starting_screen]
    
    def onTick(self, millis):
        self.getCurrentScreen().onTick(millis)
    
    def onDraw(self, g):
        self.getCurrentScreen().onDraw(g)
    
    def getCurrentScreen(self):
        return self.screens[-1]
    def setScreen(self, screen):
        self.screens.append(screen)
    def goBackNScreens(self, n):
        for i in xrange(n):
            self.screens.pop()

class UIElementContainer(Drawable):
    def __init__(self, position):
        super(UIElementContainer, self).__init__(position)
        self.ui_elements = []
    
    def onTick(self, millis):
        for elt in self.ui_elements[:]:
            elt.onTick(millis)
    
    def onDraw(self, g):
        self.draw(g)
        for elt in self.ui_elements[:]:
            elt.onDraw(g)
    
    def addChild(self, child):
        self.ui_elements.append(child)
    def removeChild(self, child):
        self.ui_elements.remove(child)

class Screen(UIElementContainer):
    def __init__(self):
        super(Screen, self).__init__(Vec2(0, 0))