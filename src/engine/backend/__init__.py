import engine
from engine.graphics import Tile, Color, Drawable
from engine.util.vector import Vec2

class Backend(object):
    def __init__(self, window_dimensions, tile_dimensions, caption, starting_screen):
        engine.window_dimensions = window_dimensions
        engine.tile_dimensions = tile_dimensions
        self.caption = caption
        self.screens = [starting_screen]
    
    def run(self):
        raise NotImplementedError()
    
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
    
    def handleKeyDown(self, event):
        self.getCurrentScreen().handleKeyDown(event)
    def handleKeyUp(self, event):
        self.getCurrentScreen().handleKeyUp(event)
    def handleMouseMoved(self, event):
        self.getCurrentScreen().handleMouseMoved(event)
    def handleMouseButtonDown(self, event):
        self.getCurrentScreen().handleMouseButtonDown(event)
    def handleMouseButtonUp(self, event):
        self.getCurrentScreen().handleMouseButtonUp(event)
    def handleMouseWheelScrolled(self, event):
        self.getCurrentScreen().handleMouseWheelScrolled(event)


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
    
    def handleKeyDown(self, event):
        self.onKeyDown(event)
        for elt in self.ui_elements[:]:
            elt.handleKeyDown(event)
    def handleKeyUp(self, event):
        self.onKeyUp(event)
        for elt in self.ui_elements[:]:
            elt.handleKeyUp(event)
    def handleMouseMoved(self, event):
        self.onMouseMoved(event)
        for elt in self.ui_elements[:]:
            elt.handleMouseMoved(event)
    def handleMouseButtonDown(self, event):
        self.onMouseButtonDown(event)
        for elt in self.ui_elements[:]:
            elt.handleMouseButtonDown(event)
    def handleMouseButtonUp(self, event):
        self.onMouseButtonUp(event)
        for elt in self.ui_elements[:]:
            elt.handleMouseButtonUp(event)
    def handleMouseWheelScrolled(self, event):
        self.onMouseWheelScrolled(event)
        for elt in self.ui_elements[:]:
            elt.handleMouseWheelScrolled(event)
    
    def onKeyDown(self, event):
        pass
    def onKeyUp(self, event):
        pass
    def onMouseMoved(self, event):
        pass
    def onMouseButtonDown(self, event):
        pass
    def onMouseButtonUp(self, event):
        pass
    def onMouseWheelScrolled(self, event):
        pass

class Screen(UIElementContainer):
    def __init__(self):
        super(Screen, self).__init__(Vec2(0, 0))