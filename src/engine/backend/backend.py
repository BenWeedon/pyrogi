class Backend(object):
    def __init__(self, game):
        self.game = game
    
    def run(self):
        raise NotImplementedError()