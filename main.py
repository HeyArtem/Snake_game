import pygame
import sys
import random
import pygame_menu # это модуль для создания меню

pygame.init() # инициализируем модуль pygame, а то шрифта для счетчика нет
bg_image = pygame.image.load('kia.jpg')     # загружаю подложку
SIZE_BLOCK = 20  # Размер блока
FRAME_COLOR = (0, 255, 204)  # Цвет поля
WHITE = (255, 255, 255)  # Цвет блока
BLUE = (204, 255, 255)  # Используется при раскрашивании кубиков через один
RED = (244, 0, 0)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0) # цвет змеи
COUNT_BLOCKS = 20  # количество блоков в нашем ряду
HEADER_MARGIN = 70
MARGIN = 1  # Отступы между кубиками
size = [SIZE_BLOCK*COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]     #[500, 600]  # Размер поля
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка Артема')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)   # шрифт и размер для счеткичика  'courier', 36., модуль font, функция SysFont

class SnakeBlock:   # координаты змейки
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    def is_inside(self): # ограничения для змейки, что бы не убагла за пределы поля
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS



    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])
def start_the_game():

    def get_random_empty_block():
        x = random.randint(0, COUNT_BLOCKS - 1)
        y = random.randint(0, COUNT_BLOCKS - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
            empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
        return empty_block

    snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)] # длина змейки, посл.коорд->голова
    apple = get_random_empty_block()
    d_row = buf_row = 0  # возможно это движение, сдвиг, змейки
    d_col = buf_col = 1
    total = 0 # счетчик очков
    speed = 0 # скорость змейки

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit, он же выход)')
                pygame.quit()
                sys.exit() # культурный выход при закрытии программы
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col != 0:
                    d_row = -1
                    d_col = 0
                elif event.key == pygame.K_DOWN and d_col != 0:
                    d_row = 1
                    d_col = 0
                elif event.key == pygame.K_LEFT and d_row != 0:
                        d_row = 0
                        d_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                        d_row = 0
                        d_col = 1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        text_total = courier.render(f'Итого: {total}', 0, WHITE) # отображение счетчика на экранеметод rendre, 0=параметр отвеч.за обтекание текстом
        text_speed = courier.render(f'СкОрОсть: {speed}', 0, WHITE) # отображение скорости на экране
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK)) # размещение на экране Итого. метод blit-> что распологаем, списком передаем где распологаем
        screen.blit(text_speed, (SIZE_BLOCK+200, SIZE_BLOCK)) # размещение на экране СкОрОсть.

        for row in range(COUNT_BLOCKS): # ряды
            for column in range(COUNT_BLOCKS): # колонки
                if (row + column) % 2 == 0:  # Раскрашиваем кубики через один, разным цветом
                    color = BLUE
                else:
                    color = WHITE

                draw_block(color, row, column)

        head = snake_blocks[-1] # возможно для движения головы- добавление новой головы
        if not head.is_inside():
            print('crash, он же ПИПЕЦ, столкнулись со стенкой)') # выход из игры, если змейка столкнулась с краем экрана
            break
            # pygame.quit()
            # sys.exit()

        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y) # рождение змейки, цвет и нач. координаты ОТРИСОВКА

        pygame.display.flip()

        if apple == head: # если яблоко пересекается с головой
            total += 1  # счетчик очков
            speed = total // 5 + 1 # за каждые сьденные 5 яблок, корость увеличивается на 1
            snake_blocks.append(apple) # добавляем яблоко в змейку
            apple = get_random_empty_block()

        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            print('crash yourself')
            # pygame.quit()
            # sys.exit()
            break

        snake_blocks.append(new_head)  # добавляем блок
        snake_blocks.pop(0)  # убираем блок, убирается конец змейки при добавлении головы


        timer.tick(3+speed)  # отрисовка кадров, будет увеличиваться со скростью






menu = pygame_menu.Menu(220, 300, '',   # размер внутреннего окна меню
                        theme=pygame_menu.themes.THEME_BLUE)

menu.add_text_input('Как тебя там :', default='Какой-то Х')
menu.add_button('В игру', start_the_game)
menu.add_button('СВАЛИТЬ от сель', pygame_menu.events.EXIT)




while True:  # размещение подложки в меню

    screen.blit(bg_image, (0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()




menu.mainloop(screen)















# 10 часть с 10 минуты, доделать изменение темы и насторить управление, почему то не идет