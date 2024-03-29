import pygame as pg

from collections import deque

import heapq


def bfs(graph, st, finish): # реализация bfs с выводом кратчайшего пути
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


def dijkstra(gr, st, finish):  # реализация dijkstra с выводом кратчайшего пути
    queue = [(False, st, [])]
    visited = set()

    while queue:
        (val, ver, path) = heapq.heappop(queue)
        if ver not in visited:
            visited.add(ver)
            path = path + [ver]
            if ver == finish:
                return path
            for curr_ver, c in gr.get(ver, ()):
                if curr_ver not in visited:
                    heapq.heappush(queue, (val + c, curr_ver, path))

    return None


def drawText(surface, color, text, where, font_name="arial", font_size=14): # реализация функции drawText для вывода текста на экран
    font = pg.font.SysFont(font_name, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if type(where) is pg.Rect:
        text_rect.center = where.center
    else:
        text_rect.topleft = where
    surface.blit(text_surface, text_rect)


# задание графа списком смежности с весами
gr = {
    0 : [(1, 5)],
    1 : [(0, 5), (2, 4)],
    2 : [(1, 4), (3, 4), (14, 3)],
    3 : [(2, 4), (4, 3)],
    4 : [(3, 3), (5, 4), (16, 3)],
    5 : [(4, 4), (6, 4)],
    6 : [(5, 4)],
    7 : [(14, 6), (15, 6)],
    8 : [(15, 5), (16, 4), (11, 4)],
    9 : [(15, 7)],
    10 : [(11, 5)],
    11 : [(10, 5), (8, 4)],
    12 : [(16, 4), (13, 4)],
    13 : [(12, 4)],
    14 : [(2, 3), (7, 6)],
    15 : [(8, 5), (7, 6), (9, 7)],
    16 : [(4, 3), (8, 4), (12, 4)]
}

# инициализация font
pg.font.init()

# задание координат левого верхенего угла, цвета и названия станции-прямоугольника
a = [(220-20, 90-50, (255, 0, 0), "Пушкинская"),
     (350-20, 130-50, (255, 0, 0), "Молодёжная"),
     (460-20, 180-50, (255, 0, 0), "Фрунзенская"),
     (550, 200, (255, 0, 0), "Немига"),
     (600, 300+70, (255, 0, 0), "Купаловская"),
     (650, 400+70, (255, 0, 0), "Первомайская"),
     (800, 500+70, (255, 0, 0), "Пролетарская"),
     (430, 260, (0, 255, 0), "Пл. Франтишка Богушевича"),
     (480, 380, (0, 0, 255), "Пл. Ленина"),
     (510, 550, (0, 255, 0), "Ковальская Слобода"),
     (120, 390, (0, 0, 255), "Грушевка"),
     (300, 450, (0, 0, 255), "Институт культуры"),
     (750, 250, (0, 0, 255), "Пл. Победы"),
     (900, 170, (0, 0, 255), "Пл. Якоба Коласа"),
     (350, 200, (0, 255, 0), "Юбилейная пл."),
     (400, 345, (0, 255, 0), "Вокзальная"),
     (570, 300, (0, 0, 255), "Октябрьская")]


# создаём сцену
screen = pg.display.set_mode((1100, 850))

# координаты концов ребер (переходов с одной станции на соседнюю)
lines = [((220-20+50, 90-50+50), (350-20, 130-50)), ((350-20+50, 130-50+50), (460-20, 180-50)), ((460-20+50, 180-50+50), (550, 200)),
         ((550+50, 200+50), (600, 300+70)), ((600+50, 300+70+50), (650, 400+70)), ((650+50, 400+70+50), (800, 500+70)),
         ((350+50, 200+50), (430, 260)), ((430+50, 260+50), (400, 345)), ((400+50, 345+50), (510, 550)),
         ((120+50, 390+50), (300, 450)), ((300+50, 450+50), (480, 380)), ((480+50, 380+50), (570, 300)), ((570+50, 300+50), (750, 250)), ((750+50, 250+50), (900, 170)),
         ((400+50, 345+50), (480, 380)), ((350+50, 200+50), (460-20, 180-50)), ((570+50, 300+50), (600, 300+70))]

# вывод ребер на экран
for i in range(len(lines)):
    pg.draw.line(screen, (255, 0, 255), lines[i][0], lines[i][1], 2)

# задание и рисовка кнопки "сбросить" внизу экрана
delete = pg.Rect(400, 750, 300, 60)
pg.draw.rect(screen, (255, 255, 255), delete)

# создаём новую поверхность
surf = pg.Surface((150, 150))
surf.set_colorkey((0, 0, 0))

# рисуем станции-прямоугольники и названия к ним
b = []
for i in range(len(a)):
    s = pg.Rect(a[i][0], a[i][1], 50, 50)
    b += [s]
    pg.draw.rect(screen, a[i][2], s)
    drawText(screen, (255, 255, 255), a[i][3], (a[i][0] - 31, a[i][1] + 50))

# задаем переменные
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
            # если попадание по кноке "сбросить", то обнуляем все параметры
            if delete.collidepoint(event.pos):
                quantity = 0
                if st != None:
                    pg.draw.rect(screen, a[st][2], b[st])
                if finish != None:
                    pg.draw.rect(screen, a[finish][2], b[finish])
                if k != None:
                    for w in k:
                        pg.draw.rect(screen, a[w][2], b[w])
                st = None
                finish = None
                k = None
            # если клик был по прямоугольнику и он 1 или 2 по счету, то эта станция становится стартом/финишом соответственно
            if quantity < 2:
                for i in range(len(b)):
                    if b[i].collidepoint(event.pos):
                        if st == None:
                            st = i
                            pg.draw.rect(screen, (219, 112, 147), b[i])
                            screen.blit(surf, pg.Rect(a[i][0], a[i][1], 50, 50))
                            quantity += 1
                        elif st != i:
                            finish = i
                            pg.draw.rect(screen, (219, 112, 147), b[i])
                            screen.blit(surf, pg.Rect(a[i][0], a[i][1], 50, 50))
                            quantity += 1
                        # если в параметрах есть и старт и финиш, то найдем и выведем кратчайший путь
                        if quantity == 2:
                            k = dijkstra(gr, st, finish)
                            for w in k:
                                pg.draw.rect(screen, (219, 112, 147), b[w])
                                screen.blit(surf, pg.Rect(a[w][0], a[w][1], 50, 50))

                        break
    # перерисовываем сцену
    pg.display.update()
    pg.time.delay(100)

pg.quit()