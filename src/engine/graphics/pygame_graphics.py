import os.path
import json
import pygame
from engine import FONT_PATH, FONT_CONFIG_EXTENSION
from engine.graphics import Graphics, Color
from engine.util.vector import Vec2

GRAYSCALE_FONT_TYPE = 'grayscale'
ALPHA_FONT_TYPE = 'alpha'

class PyGameGraphics(Graphics):
    def __init__(self):
        self.fonts = {}
    
    def init_window(self, window_dimensions, tile_dimensions, caption):
        self.screen = pygame.display.set_mode((window_dimensions*tile_dimensions).toTuple())
        self.window_dimensions = window_dimensions
        self.tile_dimensions = tile_dimensions
        pygame.display.set_caption(caption)
    
    def draw_tile(self, position, character, fg_color, bg_color):
        font_image, font_config = self._load_font('brogue.png')
        tile_image = self._get_tile_image(font_image, font_config, Vec2(0, 4), fg_color, bg_color)
        tile_image = pygame.transform.smoothscale(tile_image, self.tile_dimensions.toTuple())
        self.screen.blit(tile_image, (position*self.tile_dimensions).toTuple())
    
    def _load_font(self, filename):
        if filename not in self.fonts:
            font_image = pygame.image.load(os.path.join(FONT_PATH, filename)).convert_alpha()
            config_filename = os.path.splitext(filename)[0] + FONT_CONFIG_EXTENSION
            font_config = self._load_font_json(os.path.join(FONT_PATH, config_filename))
            if font_config.font_type == GRAYSCALE_FONT_TYPE:
                font_image = self._grayscale_to_alpha(font_image)
            self.fonts[filename] = (font_image, font_config)
        
        return self.fonts[filename]
    
    def _grayscale_to_alpha(self, image):
        for x in xrange(image.get_width()):
            for y in xrange(image.get_height()):
                color = image.get_at((x, y))
                image.set_at((x, y), (255, 255, 255, color.r))
        return image

    def _load_font_json(self, filename):
        with open(filename) as f:
            data = json.load(f)
            font_config = FontConfig(
                Vec2(data['tileWidth'], data['tileHeight']),
                data['fontType'] if 'fontType' in data else GRAYSCALE_FONT_TYPE
            )
            return font_config
    
    def _get_tile_image(self, image, config, index, fg_color, bg_color):
        dim = config.tile_dimensions
        fg_image, bg_image = self._separate_into_fg_bg(image, dim, index, fg_color, bg_color)
        tile_image = pygame.Surface((dim.x, dim.y)).convert_alpha()
        tile_image.blit(bg_image, (0, 0))
        tile_image.blit(fg_image, (0, 0))
        
        return tile_image
    
    def _separate_into_fg_bg(self, image, dim, index, fg_color, bg_color):
        fg_image = pygame.Surface((dim.x, dim.y)).convert_alpha()
        fg_image.fill((255, 255, 255, 0))
        fg_image.blit(image, (0, 0), (index.x*dim.x, index.y*dim.y, (index.x+1)*dim.x, (index.y+1)*dim.y))
        fg_image.fill(fg_color.toRGBATuple(), special_flags=pygame.BLEND_RGBA_MIN)
        
        bg_image = pygame.Surface((dim.x, dim.y)).convert()
        bg_image.fill(bg_color.toRGBTuple())
        bg_image.set_alpha(bg_color.a)
        
        return fg_image, bg_image

class FontConfig(object):
    def __init__(self, tile_dimensions, font_type):
        self.tile_dimensions = tile_dimensions
        self.font_type = font_type