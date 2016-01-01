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