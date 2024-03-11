import pygame as pg


def drawText(surface, color, text, where, font_name="Arial", font_size=16):
    font = pg.font.SysFont(font_name, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if type(where) is pg.Rect:
        text_rect.center = where.center
    else:
        text_rect.topleft = where
    surface.blit(text_surface, text_rect)

all_sprites = pg.sprite.Group()

class Stations(pg.sprite.Sprite):
    def __init__(self, coord, color, name):
        super().__init__(all_sprites)
        self.name = name
        self.coord = coord
        self.color = color
        self.img = pg.Surface((50, 50))
        self.img.fill(color)
        self.image = pg.Surface((500, 500), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

    def clck(self, pos, x, y):
        if self.rect.collidepoint(pos):
            self.rect.center = (x, y)
            return True
        return False

    def update(self):
        self.image.blit(self.img, (0, 0))