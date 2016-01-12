import random
from engine.backend import Screen
from engine.ui import Button
from engine.util.vector import Vec2
from engine.graphics import Color, LinearGradientPaint

class MainScreen(Screen):
    def __init__(self):
        super(MainScreen, self).__init__()
        
        move_button = Button(self, Vec2(2, 2), Vec2(10, 1), 'Move me!!')
        def move(elt, event):
            position = Vec2(random.randint(2, 5), random.randint(2, 5))
            elt.position = position
        move_button.set_on_clicked(move)
        move_button.base_paint = LinearGradientPaint(Color(0, 255, 0), Vec2(4, 0), Color(0, 100, 0), Vec2(-2, 0))
        self.add_child(move_button)
        
        delete_button = Button(self, Vec2(0, 0), Vec2(6, 1), 'Delete')
        def delete(elt, event):
            self.remove_child(move_button)
        delete_button.set_on_clicked(delete)
        self.add_child(delete_button)
        
        delete_self_button = Button(self, Vec2(1, 1), Vec2(11, 1), 'Delete self')
        def delete_self(elt, event):
            self.remove_child(elt)
        delete_self_button.set_on_clicked(delete_self)
        self.add_child(delete_self_button)