import pygame as pg

from collections import deque


def bfs(graph, st, finish):
    q = deque([[st]])
    visited = set()

    while q:
        path = q.popleft()
        curr = path[-1]

        if curr == finish:
            return path

        if curr not in visited:
            for near in graph[curr]:
                new_path = list(path)
                new_path.append(near)
                q.append(new_path)
            visited.add(curr)

    return None


def drawText(surface, color, text, where, font_name="arial", font_size=14):
    font = pg.font.SysFont(font_name, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if type(where) is pg.Rect:
        text_rect.center = where.center
    else:
        text_rect.topleft = where
    surface.blit(text_surface, text_rect)

# pushk = (0, 0)
# molod = (0, 0)
# frunz_yubil = (0, 0)
# nemig = (0, 0)
# kupal_octabr = (0, 0)
# pervom = (0, 0)
# prolet = (0, 0)
# frantishka = (0, 0)
# lenin_vokzal = (0, 0)
# koval = (0, 0)
# grush = (0, 0)
# inst = (0, 0)
# pobed = (0, 0)
# yakub = (0, 0)

# gr = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      1 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      2 [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#      3 [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#      4 [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
#      5 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#      6 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#      7 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#      8 [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
#      9 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#      10 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#      11 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#      12 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#      13 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

gr = [[1],
      [0, 2],
      [1, 3, 7],
      [2, 4],
      [3, 5, 8, 12],
      [4, 6],
      [5],
      [2, 8],
      [4, 7, 9, 11],
      [8],
      [11],
      [10, 8],
      [4, 13],
      [12]]

pg.font.init()

a = [(220, 90, 50, 50, (255, 0, 0), "Пушкинская"),
     (350, 130, 50, 50, (255, 0, 0), "Молодёжная"),
     (460, 180, 50, 50, (255, 0, 0), "Фрунзенская/Юбилейная пл."),
     (550, 200, 50, 50, (255, 0, 0), "Немига"),
     (600, 300, 50, 50, (255, 0, 0), "Купаловская/Октябрьская"),
     (650, 400, 50, 50, (255, 0, 0), "Первомайская"),
     (800, 500, 50, 50, (255, 0, 0), "Пролетарская"),
     (430, 260, 50, 50, (0, 255, 0), "Пл. Франтишка Богушевича"),
     (500, 340, 50, 50, (0, 255, 0), "Пл. Ленина/Вокзальная"),
     (510, 550, 50, 50, (0, 255, 0), "Ковальская Слобода"),
     (120, 390, 50, 50, (0, 0, 255), "Грушевка"),
     (350, 450, 50, 50, (0, 0, 255), "Институт культуры"),
     (750, 250, 50, 50, (0, 0, 255), "Пл. Победы"),
     (900, 170, 50, 50, (0, 0, 255), "Пл. Якоба Коласа")]


# создаём сцену
screen = pg.display.set_mode((1100, 850))

pg.draw.line(screen, (255, 255, 255), (220, 140),(350, 130), 2)
pg.draw.line(screen, (255, 255, 255), (350, 180),(460, 180), 2)
pg.draw.line(screen, (255, 255, 255), (460, 230),(550, 200), 2)
pg.draw.line(screen, (255, 255, 255), (550, 250),(600, 300), 2)
pg.draw.line(screen, (255, 255, 255), (600, 350),(650, 400), 2)
pg.draw.line(screen, (255, 255, 255), (650, 450),(800, 500), 2)
pg.draw.line(screen, (255, 255, 255), (120, 440),(350, 450), 2)
pg.draw.line(screen, (255, 255, 255), (350, 500),(500, 340), 2)
pg.draw.line(screen, (255, 255, 255), (500, 390),(600, 300), 2)
pg.draw.line(screen, (255, 255, 255), (600, 350),(750, 250), 2)
pg.draw.line(screen, (255, 255, 255), (750, 300),(900, 170), 2)
pg.draw.line(screen, (255, 255, 255), (460, 230),(430, 260), 2)
pg.draw.line(screen, (255, 255, 255), (430, 310),(500, 340), 2)
pg.draw.line(screen, (255, 255, 255), (500, 370),(510, 550), 2)




delete = pg.Rect(400, 750, 300, 60)
pg.draw.rect(screen, (255, 255, 255), delete)

# создаём новую поверхность и рисуем на ней круг
surf = pg.Surface((150, 150))
surf.set_colorkey((0, 0, 0))

b = []
for i in range(len(a)):
    s = pg.Rect(a[i][0], a[i][1], a[i][2], a[i][3])
    b += [s]
    pg.draw.rect(screen, a[i][4], s)
    drawText(screen, (255, 255, 255), a[i][5], (a[i][0] - 41, a[i][1] + a[i][3]))

quantity = 0
st = None
finish = None
k = None

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
            if delete.collidepoint(event.pos):
                quantity = 0
                if st != None:
                    pg.draw.rect(screen, a[st][4], b[st])
                if finish != None:
                    pg.draw.rect(screen, a[finish][4], b[finish])
                if k != None:
                    for w in k:
                        pg.draw.rect(screen, a[w][4], b[w])
                st = None
                finish = None
                k = None
            # если клик был по прямоугольнику, он меняет свой цвет на красный
            if quantity < 2:
                for i in range(len(b)):
                    if b[i].collidepoint(event.pos):
                        if st == None:
                            st = i
                            pg.draw.rect(screen, (219, 112, 147), b[i])
                            screen.blit(surf, pg.Rect(a[i][0], a[i][1], a[i][2], a[i][3]))
                            quantity += 1
                        elif st != i:
                            finish = i
                            pg.draw.rect(screen, (219, 112, 147), b[i])
                            screen.blit(surf, pg.Rect(a[i][0], a[i][1], a[i][2], a[i][3]))
                            quantity += 1
                        if quantity == 2:
                            k = bfs(gr, st, finish)
                            for w in k:
                                pg.draw.rect(screen, (219, 112, 147), b[w])
                                screen.blit(surf, pg.Rect(a[w][0], a[w][1], a[w][2], a[w][3]))

                        break
    # перерисовываем сцену
    pg.display.update()
    pg.time.delay(100)

pg.quit()