import random
from engine.backend import Screen
from engine.ui import Button
from engine.util.vector import Vec2

class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()
        
        move_button = Button(self, Vec2(3, 2), Vec2(10, 1), 'Move me!!')
        def move(elt, event):
            position = Vec2(random.randint(1, 5), random.randint(1, 5))
            elt.position = position
        move_button.set_on_clicked(move)
        self.add_child(move_button)
        
        delete_button = Button(self, Vec2(0, 0), Vec2(6, 1), 'Delete')
        def delete(elt, event):
            self.remove_child(move_button)
        delete_button.set_on_clicked(delete)
        self.add_child(delete_button)