import random
from engine.backend import Screen
from engine.ui import Button
from engine.util.vector import Vec2

class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()
        button = Button(self, Vec2(3, 2), Vec2(10, 2), 'test[omega]button[ram]OMG~~')
        def on_click(elt, event):
            position = Vec2(random.randint(0, 5), random.randint(0, 5))
            elt.position = position
        button.set_on_clicked(on_click)
        self.add_child(button)