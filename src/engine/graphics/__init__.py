class Graphics(object):
    def init_window(self, dimensions, tile_dimensions, caption):
        raise NotImplementedError()
    def draw_tile(self, character, fg_color, bg_color):
        raise NotImplementedError()


class Tile(object):
    def __init__(self, position, character, fg_color, bg_color):
        self.position = position
        self.character = character
        self.fg_color = fg_color
        self.bg_color = bg_color
    
    def x(self):
        return self.position.x
    def y(self):
        return self.position.y
    
    def draw(self, g):
        g.draw_tile(self.position, self.character, self.fg_color, self.bg_color)


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