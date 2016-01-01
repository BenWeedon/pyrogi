class Graphics(object):
    def init_window(self, width, height):
        raise NotImplementedError()
    def draw_tile(self, character, foreground_color, background_color):
        raise NotImplementedError()