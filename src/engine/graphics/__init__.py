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
    
    def to_RGB_tuple(self):
        return (self.r, self.g, self.b)
    def to_RGBA_tuple(self):
        return (self.r, self.g, self.b, self.a)

class Paint(object):
    def get_tile_color(self, absolute_position, relative_position):
        """absolute_position is absolute in the window, relative_position is relative_position to the Drawable being colored"""
        raise NotImplementedError()
class SolidPaint(Paint):
    def __init__(self, color):
        self.color = color
    def get_tile_color(self, absolute_position, relative_position):
        return self.color


class Drawable(object):
    def __init__(self, position):
        self.position = position
        self.tiles = []
    
    def add_tile(self, tile, offset):
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