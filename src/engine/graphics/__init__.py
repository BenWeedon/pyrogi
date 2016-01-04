class Graphics(object):
    def init_window(self, window_dimensions, tile_dimensions, caption):
        raise NotImplementedError()
    def draw_tile(self, character, fg_color, bg_color):
        raise NotImplementedError()


class Tile(object):
    def __init__(self, character, fg_color, bg_color):
        self.character = character
        self.fg_color = fg_color
        self.bg_color = bg_color
    
    def draw(self, g, position):
        g.draw_tile(position, self.character, self.fg_color, self.bg_color)


class Color(object):
    def __init__(self, r, g, b, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    
    def toRGBTuple(self):
        return (self.r, self.g, self.b)
    def toRGBATuple(self):
        return (self.r, self.g, self.b, self.a)

class Drawable(object):
    def __init__(self, position):
        self.position = position
        self.tiles = []
    
    def addTile(self, tile, offset):
        self.tiles.append((tile, offset))
    
    def draw(self, g):
        for tile, offset in self.tiles:
            tile.draw(g, self.position+offset)
    
    def contains_position(self, position):
        for tile, offset in self.tiles:
            tile_position = self.position + offset
            if tile_position == position:
                return True
        return False