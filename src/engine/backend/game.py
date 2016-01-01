import engine.graphics.tile as tile

class Game(object):
    def onTick(self, millis):
        pass
    def onDraw(self, g):
        tile.Tile(None, None, None, None).draw(g)