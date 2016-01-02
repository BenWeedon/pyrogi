import os.path
import json
import pygame
from engine import FONT_PATH, FONT_CONFIG_EXTENSION, BLACK_TUPLE, WHITE_TUPLE
from engine.graphics import Graphics
from engine.util.vector import Vec2

class PyGameGraphics(Graphics):
    def init_window(self, dimensions, caption):
        self.screen = pygame.display.set_mode((dimensions.x, dimensions.y))
        pygame.display.set_caption(caption)
    
    def draw_tile(self, position, character, fg_color, bg_color):
        font_image, font_config = self._load_font('brogue.png')
        tile_image = self._get_tile_image(font_image, font_config, Vec2(0, 4), fg_color, bg_color)
        self.screen.blit(tile_image, (0, 0))
    
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
    
    def _get_tile_image(self, image, config, index, fg_color, bg_color):
        dim = config.tile_dimensions
        fg_image, bg_image = self._separate_into_fg_bg(image, dim, index, fg_color, bg_color)
        tile_image = pygame.Surface((dim.x, dim.y)).convert()
        tile_image.blit(bg_image, (0, 0))
        tile_image.blit(fg_image, (0, 0))
        
        return tile_image
    
    def _separate_into_fg_bg(self, image, dim, index, fg_color, bg_color):
        fg_image = pygame.Surface((dim.x, dim.y)).convert()
        fg_image.set_colorkey(BLACK_TUPLE)
        fg_image.blit(image, (0, 0), (index.x*dim.x, index.y*dim.y, (index.x+1)*dim.x, (index.y+1)*dim.y))
        
        bg_image = pygame.Surface((dim.x, dim.y)).convert()
        bg_image.fill((bg_color.r, bg_color.g, bg_color.b))
        bg_image.set_alpha(bg_color.a)
        
        return fg_image, bg_image

class FontConfig(object):
    def __init__(self, tile_dimensions):
        self.tile_dimensions = tile_dimensions