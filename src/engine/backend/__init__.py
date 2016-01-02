from engine.graphics import Tile, Color
from engine.util.vector import Vec2

class Backend(object):
    def __init__(self, game):
        self.game = game
    
    def run(self):
        raise NotImplementedError()


class Game(object):
    def onTick(self, millis):
        pass
    def onDraw(self, g):
        Tile(Vec2(1, 3), None, Color(255, 255, 255, 255), Color(0, 255, 0, 255)).draw(g)
        Tile(Vec2(1, 4), None, Color(0, 255, 255, 255), Color(255, 255, 255, 255)).draw(g)
        Tile(Vec2(0, 0), None, Color(255, 255, 0, 255), Color(0, 255, 255, 255)).draw(g)
        Tile(Vec2(1, 1), None, Color(0, 0, 255, 255), Color(255, 255, 0, 255)).draw(g)
        Tile(Vec2(1, 1), None, Color(0, 0, 255, 255), Color(255, 0, 0, 100)).draw(g)
        for i in xrange(200):
            Tile(Vec2(1, 1), None, Color(0, 0, 255, 255), Color(255, 0, 0, 100)).draw(g)