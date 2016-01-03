from engine.backend import Screen
from engine.ui import TestUIElement

class TestScreen(Screen):
    def __init__(self):
        super(TestScreen, self).__init__()
        for i in xrange(30):
            self.addChild(TestUIElement())