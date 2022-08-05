# Отрисовка поля 3x3 клетки
def draw_board(spots):
    board = (
        f"\t|{spots[1]}|{spots[2]}|{spots[3]}|\n"
        f"\t|{spots[4]}|{spots[5]}|{spots[6]}|\n"
        f"\t|{spots[7]}|{spots[8]}|{spots[9]}|\n"
    )
    print(board)


# Перавыми ходят корестики. Каждый четный ход - ход ноликов
def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


def check_for_win(spots):
    # Проверка выигрышных совпадений по горизонтали
    if (spots[1] == spots[2] == spots[3]) or (spots[4] == spots[5] == spots[6]) or (spots[7] == spots[8] == spots[9]):
        return True

    # Проверка выигрышных совпадений по вертикали
    elif (spots[1] == spots[4] == spots[7]) or (spots[2] == spots[5] == spots[8]) or (spots[3] == spots[6] == spots[9]):
        return True

    # Проверка выигрышных совпадений по диагонали
    elif (spots[1] == spots[5] == spots[9]) or (spots[7] == spots[5] == spots[3]):
        return True

    else:
        return False
