from engine.backend import Screen
from engine.ui import Button
from engine.util.vector import Vec2

class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()
        for i in xrange(30):
            self.add_child(Button(self, Vec2(3, 2), Vec2(10, 2), 'test[omega]button[ram]OMG~~'))