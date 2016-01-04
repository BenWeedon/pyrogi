from engine.backend.pygame_backend import PyGameBackend
from engine.util.vector import Vec2
from test_game import TestScreen

PyGameBackend(Vec2(20, 20), Vec2(19, 33), '', TestScreen()).run()