class Graphics(object):
    def init_window(self, width, height, caption):
        raise NotImplementedError()
    def draw_tile(self, character, fg_color, bg_color):
        raise NotImplementedError()