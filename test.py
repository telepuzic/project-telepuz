import pygame as pg

# создаём сцену
screen = pg.display.set_mode((1080, 920))

# рисуем прямоугольник
rect_big = pg.Rect(100, 100, 200, 500)
pg.draw.rect(screen, (255, 255, 0), rect_big)

# создаём новую поверхность и рисуем на ней круг
surf = pg.Surface((150, 150))
surf.set_colorkey((0, 0, 0))
pg.draw.circle(surf, (255, 255, 255), (75, 75), 75)
screen.blit(surf, pg.Rect(150, 150, 150, 150))

# основной цикл программы
running = True
while running:
    # получаем список произошедших событий из очереди
    events = pg.event.get()
    for event in events:
        # если в списке есть событие pg.QUIT, завершаем работу программы
        if event.type == pg.QUIT:
            running = False
        # если была нажата кнопка мыши (любая), то проверяем координаты клика
        if event.type == pg.MOUSEBUTTONDOWN:
            # если клик был по прямоугольнику, он меняет свой цвет на красный
            if rect_big.collidepoint(event.pos):
                pg.draw.rect(screen, (255, 0, 0), rect_big)
                screen.blit(surf, pg.Rect(150, 150, 150, 150))
    # перерисовываем сцену
    pg.display.update()
    pg.time.delay(100)

pg.quit()