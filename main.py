import pygame as pg
from circles import *


FPS = 60
WIDTH = 1300
HEIGHT = 700
pg.init()
SIZE = (WIDTH, HEIGHT)
screen = pg.display.set_mode(SIZE)
circle = Circles(200, 200, (150, 0, 0), "dthrth")
all_sprites = pg.sprite.Group()
all_sprites.add(circle)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pg.display.update()
    pg.time.delay(100)

pg.quit()