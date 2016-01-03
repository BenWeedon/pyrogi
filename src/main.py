from engine.backend.pygame_backend import PyGameBackend
from engine.backend import Game
from engine.util.vector import Vec2
from test_game import TestScreen

PyGameBackend(Game(TestScreen()), Vec2(20, 20), Vec2(30, 30), '').run()