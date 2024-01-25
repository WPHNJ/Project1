import pygame
import random
import sys
import os
import time

########################################################################################################################


def file_filler():
    f = open("уровень.txt", 'w')
    for _ in range(125):
        for _ in range(125):
            print(f.write(random.choice('10')))
        print(f.write('\n'))
    f.close()


def level_smoother():
    for _ in range(5):
        f = open("уровень.txt", 'r')
        k = f.read()
        f.close()
        li = k.split()
        li1 = []
        for x in range(0, len(li)):
            li1.append([])
            for y in range(0, len(li)):
                counter_floar = 0
                counter_wall = 0
                if x != 0 and y != 0 and x != len(li) - 1 and y != len(li) - 1:
                    if li[x - 1][y - 1] == '0':
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if li[x - 1][y] == '0':
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if li[x - 1][y + 1] == "0":
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if li[x][y - 1] == "0":
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if li[x][y] == "0":
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if li[x][y + 1] == "0":
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if li[x + 1][y - 1] == "0":
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if li[x + 1][y] == "0":
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if li[x + 1][y + 1] == "0":
                        counter_floar += 1
                    else:
                        counter_wall += 1

                    if counter_wall <= counter_floar:
                        li1[-1].append(0)
                    else:
                        li1[-1].append(1)
                else:
                    li1[-1].append(1)
        print(li1)
        f = open("уровень.txt", 'w')
        for i in li1:
            for j in i:
                print(f.write(str(j)))
            print(f.write('\n'))
        f.close()


def rocks_creator():
    f = open("уровень.txt", 'r')
    k = f.read()
    f.close()
    li = k.split()
    li1 = []
    for x in range(0, len(li)):
        li1.append([])
        for y in range(0, len(li)):
            if li[x][y] == "1":
                li1[-1].append("1")
            else:
                li1[-1].append(random.choice('200000000000000000'))
    print(li1)
    f = open("уровень.txt", 'w')
    for i in li1:
        for j in i:
            print(f.write(str(j)))
        print(f.write('\n'))
    f.close()
    print(li1)


def ors_creator():
    f = open("уровень.txt", 'r')
    k = f.read()
    f.close()
    li = k.split()
    li1 = []
    for x in range(0, len(li)):
        li1.append([])
        for y in range(0, len(li)):
            if li[x][y] == "1":
                li1[-1].append("1")
            elif li[x][y] == "2":
                li1[-1].append("2")
            else:
                li1[-1].append(random.choice('3000000000'))
    print(li1)
    f = open("уровень.txt", 'w')
    for i in li1:
        for j in i:
            print(f.write(str(j)))
        print(f.write('\n'))
    f.close()
    print(li1)


def player_creator():
    f = open("уровень.txt", 'r')
    k = f.read()
    f.close()
    li = k.split()
    li1 = []
    r = 0
    for x in range(0, len(li)):
        li1.append([])
        for y in range(0, len(li)):
            if li[x][y] == "1":
                li1[-1].append("1")
            elif li[x][y] == "2":
                li1[-1].append("2")
            elif li[x][y] == "3":
                li1[-1].append("3")
            else:
                if r != "4":
                    r = '4'
                    li1[-1].append(r)
                else:
                    li1[-1].append('0')
    print(li1)
    f = open("уровень.txt", 'w')
    for i in li1:
        for j in i:
            print(f.write(str(j)))
        print(f.write('\n'))
    f.close()
    print(li1)


def ex_creator():
    f = open("уровень.txt", 'r')
    k = f.read()
    f.close()
    li = k.split()
    li.reverse()
    for i in range(len(li)):
        li[i] = li[i][::-1]
    li1 = []
    r = 0
    for x in range(0, len(li)):
        li1.append([])
        for y in range(0, len(li)):
            if r != "5" and x == 1 and y == 1:
                r = '5'
                li1[-1].append(r)
            else:
                if li[x][y] == "1":
                    li1[-1].append("1")
                elif li[x][y] == "2":
                    li1[-1].append("2")
                elif li[x][y] == "3":
                    li1[-1].append("3")
                elif li[x][y] == "4":
                    li1[-1].append("4")
                else:
                    li1[-1].append('0')
    print(li1)
    f = open("уровень.txt", 'w')
    for i in li1:
        for j in i:
            print(f.write(str(j)))
        print(f.write('\n'))
    f.close()
    print(li1)


def ways_creator():
    f = open("уровень.txt", 'r')
    k = f.read()
    f.close()
    li = k.split()
    player = []
    ex = []
    li1 = []
    for x in range(0, len(li)):
        for y in range(0, len(li)):
            if li[x][y] == "4":
                player = [x, y]
            elif li[x][y] == "5":
                ex = [x, y]
    for x in range(0, len(li)):
        li1.append([])
        for y in range(0, len(li)):
            if li[x][y] == "1":
                li1[-1].append("1")
            elif li[x][y] == "2":
                li1[-1].append("2")
            elif li[x][y] == "3":
                li1[-1].append("3")
            elif li[x][y] == "4":
                li1[-1].append("4")
            elif li[x][y] == "5":
                li1[-1].append("5")
            else:
                li1[-1].append('0')
    xes = int(player[0]) - int(ex[0])
    yes = int(player[1]) - int(ex[1])
    way_maker = ""
    for i in range(xes - 1):
        way_maker += "r"
    for j in range(yes - 1):
        way_maker += "d"
    way_maker = random.sample(way_maker, len(way_maker))
    print(player, ex, way_maker)
    for i in range(len(way_maker)):
        if way_maker[i] == "d":
            li1[int(ex[0])][int(ex[1]) + 1] = 0
            ex[1] = int(ex[1]) + 1
        else:
            li1[int(ex[0]) + 1][int(ex[1])] = 0
            ex[0] = int(ex[0]) + 1
    f = open("уровень.txt", 'w')
    for i in li1:
        for j in i:
            print(f.write(str(j)))
        print(f.write('\n'))
    f.close()
    print(player, ex, way_maker)


file_filler()
level_smoother()
rocks_creator()
ors_creator()
player_creator()
ex_creator()
ways_creator()

########################################################################################################################


def load_image(name, color_key=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
sprite_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()

tile_images = {
    'wall': load_image('stone.png'),
    'dirt': load_image('dirt.png'),
    'ore': load_image('ore.png'),
    'stone': load_image('small_stone.png'),
    'hole': load_image('hole.png')
}
player_image = load_image('mario.png')

tile_width = tile_height = 50


class ScreenFrame(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = (0, 0, 800, 400)


class SpriteGroup(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def get_event(self, event):
        for i in self:
            i.get_event(event)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.rect = None

    def get_event(self, event):
        pass


class Tile(Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hero_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(tile_width * self.pos[0] + 15,
                                               tile_height * self.pos[1] + 5)


class Camera:
    def __init__(self):
        x, y = hero.pos
        self.dx = x
        self.dy = y

    def apply(self, obj):
        obj.rect.x += self.dx * 50
        obj.rect.y += self.dy * 50

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)

    def update_up(self, target):
        self.dx = 0
        self.dy = 1

    def update_down(self, target):
        self.dx = 0
        self.dy = -1

    def update_right(self, target):
        self.dx = -1
        self.dy = 0

    def update_left(self, target):
        self.dx = 1
        self.dy = 0


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Cave Game", '',
                  "Цель - дойти до дыры"]
    fon = pygame.transform.scale(load_image('dirt.png'), size)
    screen.blit((fon), (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


def end_screen():
    intro_text = ["Cave Game", '',
                  f"Время - {time.time() - seconds} секунды"]
    fon = pygame.transform.scale(load_image('dirt.png'), size)
    screen.blit((fon), (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                file_filler()
                level_smoother()
                rocks_creator()
                ors_creator()
                player_creator()
                ex_creator()
                ways_creator()
                global level_map
                level_map = load_level('уровень.txt')
                hero, max_x, max_y = generate_level(level_map)
                for sprite in sprite_group:
                    print(sprite)
                print(sprite_group)
                camera = Camera()
                print(hero.pos)
                if hero in sprite_group:
                    print(111)
                camera.update(hero)
                return
        pygame.display.flip()


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '1')), level_map))


def generate_level(level):
    new_player = 0
    x = 0
    y = 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '0':
                Tile('dirt', x, y)
            elif level[y][x] == '1':
                Tile('wall', x, y)
            elif level[y][x] == '2':
                Tile('stone', x, y)
            elif level[y][x] == '3':
                Tile('ore', x, y)
            elif level[y][x] == '4':
                Tile('hole', x, y)
            elif level[y][x] == '5':
                Tile('dirt', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def move(hero, movement):
    x, y = hero.pos
    if movement == 'up':
        if y > 0 and (level_map[y - 1][x] == '0' or level_map[y - 1][x] == '4' or level_map[y - 1][x] == '5'):
            print(2)
            camera.update_up(hero)
            for sprite in sprite_group:
                camera.apply(sprite)
            hero.pos = x, y - 1
    elif movement == 'down':
        if y < max_y - 1 and (level_map[y + 1][x] == '0' or level_map[y + 1][x] == '4' or level_map[y + 1][x] == '5'):
            print(2)
            camera.update_down(hero)
            for sprite in sprite_group:
                camera.apply(sprite)
            hero.pos = x, y + 1
    elif movement == 'left':
        if x > 0 and (level_map[y][x - 1] == '0' or level_map[y][x - 1] == '4' or level_map[y][x - 1] == '5'):
            camera.update_left(hero)
            for sprite in sprite_group:
                camera.apply(sprite)
            hero.pos = x - 1, y
    elif movement == 'right':
        if x < max_x - 1 and (level_map[y][x + 1] == '0' or level_map[y][x + 1] == '4' or level_map[y][x + 1] == '5'):
            camera.update_right(hero)
            for sprite in sprite_group:
                camera.apply(sprite)
            hero.pos = x + 1, y
    if level_map[y][x] == '4':
        end_screen()
        hero.pos = (1, 1)


if __name__ == '__main__':
    running = True
    start_screen()
    level_map = load_level('уровень.txt')
    hero, max_x, max_y = generate_level(level_map)
    for sprite in sprite_group:
        print(sprite)
    print(sprite_group)
    camera = Camera()
    print(hero.pos)
    if hero in sprite_group:
        print(111)
    camera.update(hero)
    seconds = time.time()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print(1)
                    move(hero, 'up')
                if event.key == pygame.K_DOWN:
                    print(1)
                    move(hero, 'down')
                if event.key == pygame.K_RIGHT:
                    move(hero, 'right')
                if event.key == pygame.K_LEFT:
                    move(hero, 'left')

        screen.fill(pygame.Color('black'))
        print(hero.pos)
        sprite_group.draw(screen)
        hero_group.draw(screen)
        pygame.display.flip()
    pygame.quit()
