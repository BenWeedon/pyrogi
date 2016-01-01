import pygame
import engine.graphics.graphics as graphics
import engine.util.vector as vector

class PyGameGraphics(graphics.Graphics):
    def init_window(self, dimensions, caption):
        self.screen = pygame.display.set_mode((dimensions.x, dimensions.y))
        pygame.display.set_caption(caption)
    
    def draw_tile(self, position, character, fg_color, bg_color):
        font_image = pygame.image.load('res/font.png').convert()
        tile_image = self._get_tile_image(font_image, vector.Vec2(0, 0))
        self.screen.blit(tile_image, (0, 0))
        pygame.display.update()
    
    def _get_tile_image(self, image, index):
        tile_image = pygame.Surface((10, 10)).convert()
        tile_image.blit(image, (0, 0), (index.x*10, index.y*10, (index.x+1)*10, (index.y+1)*10))
        return tile_image