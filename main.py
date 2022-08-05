from helpers import draw_board, check_turn, check_for_win

# Клетки поля
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

print('\n*** Крестики-нолики ***')
print('------------------------\n')

playing = True
completed = False

# Счетчик ходов. Первымии ходят крестики
turn = 0
prev_turn = -1

# № Запуск игры
while playing:
    # Отрисовка поля с ожиданием хода игрока или выхода из игры
    draw_board(spots)
    # Проверка существония клетки и свободна ли она
    if prev_turn == turn:
        print('*** Ошибка ввода ***')
        print('Клетки не существует или уже занята. Поопробуйте еще раз.')
    prev_turn = turn
    # Первыми ходят креестики и дальше по очереди.
    if turn % 2 == 0:
        choice = input('Ходят крестики. Введите номер клетки или "q" для выхода: ')
    else:
        choice = input('Ходят нолики. Введите номер клетки или "q" для выхода: ')
    # Выход из игры
    if choice == 'q':
        playing = False
    # Проверка ввода(Введена ли цифра и существует ли такая клетка)
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {'X', 'O'}:
            # Ход засчитан, клетка обновляется
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # Проверка конца игры
    if check_for_win(spots):
        playing, completed = False, True

    # Обработка ничьей
    if turn == 9:
        playing = False
        print('Ходов больше нет. Победила ничья.')


draw_board(spots)

# Объявление победителя
if completed:
    if check_turn(turn) == 'X':
        print('Поздравляем, победили крестики!')
    elif check_turn(turn) == 'O':
        print('Поздравляем, победили нолики!')
    else:
        print('Поздравляем,, победила ничья!')

print('Спасибо за игру!')
