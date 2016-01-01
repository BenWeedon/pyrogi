import pygame
from engine.graphics.pygame_graphics import PyGameGraphics
from engine.backend import Backend
from engine.util.vector import Vec2

FRAMERATE = 60

class PyGameBackend(Backend):
    def __init__(self, game):
        super(PyGameBackend, self).__init__(game)
        pygame.init()
    
    def run(self):
        clock = pygame.time.Clock()
        g = PyGameGraphics()
        g.init_window(Vec2(500, 500), '')
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            
            fps = clock.get_fps()
            pygame.display.set_caption('FPS: ' + str(fps))
            
            millis = clock.tick(FRAMERATE)
            self.game.onTick(millis)
            self.game.onDraw(g)