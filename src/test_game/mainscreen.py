from engine.backend import Screen
from engine.ui import TestUIElement

class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()
        for i in xrange(30):
            self.addChild(TestUIElement(self, None, None))