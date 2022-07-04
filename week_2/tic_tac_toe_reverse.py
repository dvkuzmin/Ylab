import pygame
from typing import List, Tuple
from random import choice
import sys


pygame.init()

SIZE_BLOCK = 60
MARGIN = 2
WIDTH = HEIGHT = SIZE_BLOCK * 10 + MARGIN * 11

BLACK = (0, 0, 0)
X_COLOR = (81, 180, 107)
O_COLOR = (217, 121, 50)
WHITE = (255, 255, 255)

size_window = WIDTH, HEIGHT

screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Обратные крестики-нолики")

game_over_text = ''

matrix = [[0] * 10 for _ in range(10)]
available_cells = []

for i in range(10):
    for j in range(10):
        available_cells.append((i, j))


def check_loose(matrix: List[List[int]], mark: str, coord: Tuple[int, int]):
    x = coord[1]
    y = coord[0]

    counter = 1
    coord_x = x + 1

    while coord_x < len(matrix) and matrix[y][coord_x] == mark: # horizontal line check
        counter += 1
        coord_x += 1
        if counter >= 5:
            return True

    coord_x = x - 1

    while coord_x >= 0 and matrix[y][coord_x] == mark:
        counter += 1
        coord_x -= 1
        if counter >= 5:
            return True

    counter = 1
    coord_y = y - 1

    while coord_y >= 0 and matrix[coord_y][x] == mark:  # vertical line check
        counter += 1
        coord_y -= 1
        if counter >= 5:
            return True

    coord_y = y + 1

    while coord_y < len(matrix) and matrix[coord_y][x] == mark:
        counter += 1
        coord_y += 1
        if counter >= 5:
            return True

    counter = 1
    coord_x = x + 1
    coord_y = y + 1

    # left diagonal line check
    while coord_y < len(matrix) and coord_x < len(matrix) and matrix[coord_y][coord_x] == mark:
        counter += 1
        coord_x += 1
        coord_y += 1
        if counter >= 5:
            return True

    coord_x = x - 1
    coord_y = y - 1

    while coord_y >= 0 and coord_x >= 0 and matrix[coord_y][coord_x] == mark:
        counter += 1
        coord_x -= 1
        coord_y -= 1
        if counter >= 5:
            return True

    counter = 1
    coord_x = x - 1
    coord_y = y + 1

    #  right diagonal line check
    while coord_y < len(matrix) and coord_x >= 0 and matrix[coord_y][coord_x] == mark:
        counter += 1
        coord_x -= 1
        coord_y += 1
        if counter >= 5:
            return True

    coord_x = x + 1
    coord_y = y - 1

    while coord_y >= 0 and coord_x < len(matrix) and matrix[coord_y][coord_x] == mark:
        counter += 1
        coord_x += 1
        coord_y -= 1
        if counter >= 5:
            return True


def computer_move():
    global game_over_text

    available_cells_copy = available_cells.copy()

    while True:
        coord = choice(available_cells_copy)
        available_cells_copy.remove(coord)
        row = coord[0]
        col = coord[1]
        matrix[row][col] = 'o'
        if check_loose(matrix, 'o', (row, col)):
            if available_cells_copy:
                matrix[row][col] = 0
                continue
            else:
                matrix[row][col] = 'o'
                game_over_text = "You win! Congrats!"
                break
        else:
            if len(available_cells) == 0:
                game_over_text = "Draw! Friendship wins!"
            else:
                available_cells.remove(coord)
                break


def main_loop():
    global game_over_text
    global matrix
    global available_cells

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over_text:
                player_move()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_over_text:
                game_over_text = ''
                matrix = [[0] * 10 for _ in range(10)]
                available_cells = []
                screen.fill(BLACK)

                for i in range(10):
                    for j in range(10):
                        available_cells.append((i, j))

        draw_field()


def player_move():
    global game_over_text

    x_mouse, y_mouse = pygame.mouse.get_pos()
    col = x_mouse // (SIZE_BLOCK + MARGIN)
    row = y_mouse // (SIZE_BLOCK + MARGIN)

    if matrix[row][col] == 0:
        available_cells.remove((row, col))
        matrix[row][col] = 'x'
        if check_loose(matrix, 'x', (row, col)):
            game_over_text = "You loose! See you next time!"
        computer_move()


def draw_field():
    for row in range(10):
        for col in range(10):
            color = WHITE
            if matrix[row][col] == 'x':
                color = X_COLOR
            elif matrix[row][col] == 'o':
                color = O_COLOR
            x = col * SIZE_BLOCK + (col + 1) * MARGIN
            y = row * SIZE_BLOCK + (row + 1) * MARGIN
            pygame.draw.rect(screen, color, (x, y, SIZE_BLOCK, SIZE_BLOCK))
            if matrix[row][col] == 'x':
                pygame.draw.line(screen, BLACK, (x+5, y+5), (x+SIZE_BLOCK-5, y+SIZE_BLOCK-5), 2)
                pygame.draw.line(screen, BLACK, (x+SIZE_BLOCK-5, y+5), (x+5, y+SIZE_BLOCK-5), 2)
            elif matrix[row][col] == 'o':
                pygame.draw.circle(screen, BLACK, (x+SIZE_BLOCK//2, y+SIZE_BLOCK//2), SIZE_BLOCK//2-5, 2)

    if game_over_text:
        # screen.fill(WHITE)
        font = pygame.font.SysFont('stxingkai', 30)
        text = font.render(game_over_text + " Press space to try again", True, BLACK)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        pygame.draw.rect(screen, WHITE, (text_x, text_y, text_rect.width, text_rect.height))
        screen.blit(text, [text_x, text_y])

    pygame.display.update()


if __name__ == "__main__":
    main_loop()
