from engine.backend.pygame_backend import PyGameBackend
from engine.backend import Game
from test_game import TestScreen

PyGameBackend(Game(TestScreen())).run()