import os.path
import json
import pygame
from engine import FONT_PATH, FONT_CONFIG_EXTENSION
from engine.graphics import Graphics
from engine.util.vector import Vec2

class PyGameGraphics(Graphics):
    def init_window(self, dimensions, caption):
        self.screen = pygame.display.set_mode((dimensions.x, dimensions.y))
        pygame.display.set_caption(caption)
    
    def draw_tile(self, position, character, fg_color, bg_color):
        font_image, font_config = self._load_font('brogue.png')
        tile_image = self._get_tile_image(font_image, font_config, Vec2(0, 4))
        self.screen.blit(tile_image, (0, 0))
        pygame.display.update()
    
    def _load_font(self, filename):
        font_image = pygame.image.load(os.path.join(FONT_PATH, filename)).convert()
        config_filename = os.path.splitext(filename)[0] + FONT_CONFIG_EXTENSION
        font_config = self._load_font_json(os.path.join(FONT_PATH, config_filename))
        
        return font_image, font_config

    def _load_font_json(self, filename):
        with open(filename) as f:
            data = json.load(f)
            font_config = FontConfig(
                Vec2(data['tileWidth'], data['tileHeight'])
            )
            return font_config
    
    def _get_tile_image(self, image, config, index):
        dim = config.tile_dimensions
        tile_image = pygame.Surface((dim.x, dim.y)).convert()
        tile_image.blit(image, (0, 0), (index.x*dim.x, index.y*dim.y, (index.x+1)*dim.x, (index.y+1)*dim.y))
        return tile_image

class FontConfig(object):
    def __init__(self, tile_dimensions):
        self.tile_dimensions = tile_dimensions