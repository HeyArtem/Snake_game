import pygame
import sys

SIZE_BLOCK = 20  # Размер блока
FRAME_COLOR = (0, 255, 204)  # Цвет поля
WHITE = (255, 255, 255)  # Цвет блока
BLUE = (204, 255, 255)  # Используется при раскрашивании кубиков через один
SNAKE_COLOR = (0, 102, 0) # цвет змеи
HEADER_COLOR = (0, 204, 153)
COUNT_BLOCKS = 20  # количество блоков в нашем ряду
HEADER_MARGIN = 70
MARGIN = 1  # Отступы между кубиками
size = [SIZE_BLOCK*COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]     #[500, 600]  # Размер поля
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка Артема')
timer = pygame.time.Clock()

class SnakeBlock:   # координаты змейки
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    def is_insite(self): # ограничения для змейки, что бы не убагла за пределы поля
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK




def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])

snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)] # длина змейки, посл.коорд->голова

d_row = 0  # возможно это движение, сдвиг, змейки
d_col = 1

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

    for row in range(COUNT_BLOCKS): # ряды
        for column in range(COUNT_BLOCKS): # колонки
            if (row + column) % 2 == 0:  # Раскрашиваем кубики через один, разным цветом
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, column)
    head = snake_blocks[-1]
    if not head.is_insite():
        print('crash, он же ПИПЕЦ, столкнулись со стенкой)') # выход из игры, если змейка столкнулась с краем экрана
        pygame.quit()
        sys.exit()

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y) # рождение змейки, цвет и нач. координаты ОТРИСОВКА

    head = snake_blocks[-1]  # возможно для движения головы- добавление новой головы
    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)  # добавляем блок
    snake_blocks.pop(0)  # убираем блок, убирается конец змейки при добавлении головы


    pygame.display.flip()
    timer.tick(2)


# закончил часть 6