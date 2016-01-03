from engine.graphics import Tile, Color
from engine.util.vector import Vec2

class Backend(object):
    def __init__(self, game):
        self.game = game
    
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

class UIElementContainer(object):
    def __init__(self):
        self.ui_elements = []
    
    def onTick(self, millis):
        for elt in self.ui_elements[:]:
            elt.onTick(millis)
    
    def onDraw(self, g):
        for elt in self.ui_elements[:]:
            elt.onDraw(g)
    
    def addChild(self, child):
        self.ui_elements.append(child)
    def removeChild(self, child):
        self.ui_elements.remove(child)

class Screen(UIElementContainer):
    pass