from engine.graphics import Tile, Color

class Backend(object):
    def __init__(self, game):
        self.game = game
    
    def run(self):
        raise NotImplementedError()


class Game(object):
    def onTick(self, millis):
        pass
    def onDraw(self, g):
        Tile(None, None, Color(255, 255, 255, 255), Color(0, 255, 0, 255)).draw(g)