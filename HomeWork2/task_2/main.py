import sys
import pygame
from random import choice
from my_algorims import proverka, visual_matrix  # для проверки матрицы нужно было
'''
Оствил в консоле вывод матрицы матрицы, а так же длину словаря из оставшихся возможных вершин 
Может быть будет полезно вам для тестов или отладки.
'''

pygame.init()
size_block = 50
margin = 1

width = size_block * 10 + margin * 11
height = size_block * 10 + margin * 11

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-Нолики. P.S. Нажми пробел, чтобы начать заного.')

black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (190, 190, 190)

matrix = [['-'] * 10 for i in range(10)]
query = 0
game_over = False
symbol = 'O'
count_attempts = 5

dictionary = {}
for i in range(10):
    for j in range(10):
        dictionary[(i, j)] = (i, j)
flag = False
# visual_matrix(matrix)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)  # Координаты х и у по клику(но надо сделать, чтобы было от робота)
            row = y_mouse // (size_block + margin)
            if matrix[row][col] == '-':  # Массив из прочерков
                if query % 2 == 0:
                    matrix[row][col] = 'X'
                    dictionary.pop(dictionary.get((row, col)), None)  # удаление элемента из словаря
                    print(len(dictionary))
                    visual_matrix(matrix)
                    query += 1
                    flag = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            matrix = [['-'] * 10 for i in range(10)]
            query = 0
            screen.fill(black)
            dictionary = {}
            for i in range(10):
                for j in range(10):
                    dictionary[(i, j)] = (i, j)
        elif flag:  # Здесь алгоритм компа, почти ИИ)
            good_choice = choice(list(dictionary.keys()))
            row, col = good_choice[0], good_choice[1]
            matrix[row][col] = 'O'
            mb_ans = dictionary.pop(dictionary.get((row, col)), None)  # переменная для добавления в массив неудачных точек
            print()
            print(len(dictionary))
            query += 1
            visual_matrix(matrix)
            if proverka(matrix, 'O') == f'Проиграл игрок с элементом "{symbol}"':  # или даже тут начинается ии))
                print('погоди, я ещё подумаю')
                bad_choice = []
                count = 0
                bad_choice.append((row, col))
                matrix[row][col] = '-'
                for i in range(count_attempts - 1):  # кол-во попыток выбрать новую точку, чтобы не програть щас
                    if len(dictionary) > 0:
                        good_choice = choice(list(dictionary.keys()))  # заного выбираем точку
                        row, col = good_choice[0], good_choice[1]
                        matrix[row][col] = 'O'
                        mb_ans = dictionary.pop(dictionary.get((row, col)), None)  # вырезаем и отождествляем точку (x, y)
                        if proverka(matrix, 'O') != f'Проиграл игрок с элементом "{symbol}"':
                            bad_choice.append(mb_ans)
                            print('А куда ведёт этот брейк?')
                            break
                        else:
                            count += 1
                            print(f'{count} попытка')
                            matrix[row][col] = '-'
                            bad_choice.append(mb_ans)

                    else:
                        matrix[row][col] = 'O'
                        print('Ну я пытался')
                for cord in bad_choice[:-1]:
                    dictionary[cord] = cord

            flag = False
    if not game_over:  # мб потом убрать этот иф
        for row in range(10):
            for col in range(10):
                if matrix[row][col] == 'X':
                    color = red
                elif matrix[row][col] == 'O':
                    color = blue
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, black, (x+10, y + 10), (x + size_block-10, y + size_block-10), 3)
                    pygame.draw.line(screen, black, (x + size_block-10, y + 10), (x + 5, y + size_block-10), 3)
                elif color == blue:
                    pygame.draw.circle(screen, black, (x + size_block // 2, y + size_block // 2), size_block // 2 - 10, 3)

    if len(dictionary) == 0:  # проверка на окончание игры
        game_over = 'Ничья'
    else:
        if (query - 1) % 2 == 0:  # я , т.е. крестики
            game_over = proverka(matrix, 'X')
        elif (query - 1) % 2 == 1:  # не я(бот)
            game_over = proverka(matrix, 'O')

    if game_over:
        flag = False
        screen.fill(black)
        font = pygame.font.SysFont('stxingkai', 40)
        text_1 = font.render(game_over, True, white)  # текст, который выводится при конце игры
        text_rect = text_1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2  # координаты х и у
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text_1, [text_x, text_y])

    pygame.display.update()
