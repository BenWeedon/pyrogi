import pygame
import graphics

class PyGameGraphics(graphics.Graphics):
    def init_window(self, width, height, caption):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
    
    def draw_tile(self, character, fg_color, bg_color):
        image = pygame.image.load('res/font.png').convert()
        self.screen.blit(image, (0, 0))
        pygame.display.update()