import pygame
import engine.graphics.pygame_graphics as graphics
import engine.backend.backend as backend
import engine.util.vector as vector

FRAMERATE = 60

class PyGameBackend(backend.Backend):
    def __init__(self, game):
        super(PyGameBackend, self).__init__(game)
        pygame.init()
    
    def run(self):
        clock = pygame.time.Clock()
        g = graphics.PyGameGraphics()
        g.init_window(vector.Vec2(500, 500), '')
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break
            
            fps = clock.get_fps()
            pygame.display.set_caption('FPS: ' + str(fps))
            
            millis = clock.tick(FRAMERATE)
            self.game.onTick(millis)
            self.game.onDraw(g)