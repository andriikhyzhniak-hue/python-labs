
def print_field(field, player_x, player_y):
    print("\nИгровое поле:")

    for y in range(len(field)):
        for x in range(len(field[y])):
            if x == player_x and y == player_y:
                print("P", end=" ")
            else:
                print(field[y][x], end=" ")
        print()


def input_key():
    key = input("\nНаправление (WASD, QEZC) или X - выход: ")
    return key.lower()


def move_player(key, player_x, player_y, field):
    directions = {
        "w": (0, -1),
        "s": (0, 1),
        "a": (-1, 0),
        "d": (1, 0),
        "q": (-1, -1),
        "e": (1, -1),
        "z": (-1, 1),
        "c": (1, 1)
    }

    if key not in directions:
        return player_x, player_y, False, False

    dx, dy = directions[key]

    while True:
        new_x = player_x + dx
        new_y = player_y + dy

        # Перевірка меж поля та стін
        if (not (0 <= new_x < len(field[0]) and
                 0 <= new_y < len(field)) or
                field[new_y][new_x] == "#"):
            break

        player_x = new_x
        player_y = new_y

        # Перевірка пастки
        if field[player_y][player_x] == "X":
            return player_x, player_y, True, False

        # Перевірка призу
        if field[player_y][player_x] == "*":
            field[player_y][player_x] = "."

        # Перевірка клітини зупинки
        if field[player_y][player_x] == "O":
            break

    return player_x, player_y, False, True


def count_prizes(field):
    total = 0

    for row in field:
        for cell in row:
            if cell == "*":
                total += 1

    return total


def main():
    field = [
        list("#########"),
        list("#...*...#"),
        list("#.......#"),
        list("#..#....#"),
        list("#O...X.O#"),
        list("#.......#"),
        list("#...*...#"),
        list("#.......#"),
        list("#########")
    ]

    player_x = 1
    player_y = 1

    score = 0
    moves = 0
    game_over = False

    print("================================")
    print("       ИГРА INERTIA")
    print("================================")
    print("Собери все призы и не попади в ловушку!")
    print("W - вверх, S - вниз")
    print("A - влево, D - вправо")
    print("Q - вверх-влево, E - вверх-вправо")
    print("Z - вниз-влево, C - вниз-вправо")
    print("X - выход из игры")

    while not game_over:

        print_field(field, player_x, player_y)

        print("Собрано призов:", score)
        print("Осталось призов:", count_prizes(field))
        print("Количество ходов:", moves)

        key = input_key()

        if key == "x":
            print("Вы вышли из игры.")
            break

        if key not in ["w", "a", "s", "d",
                       "q", "e", "z", "c"]:
            print("Неверная команда!")
            continue

        old_x = player_x
        old_y = player_y

        player_x, player_y, lost, moved = move_player(
            key, player_x, player_y, field
        )

        if moved:
            moves += 1

        if lost:
            print_field(field, player_x, player_y)
            print("Вы попали в ловушку!")
            print("Игра окончена. Вы проиграли!")
            game_over = True
            break

        score = 2 - count_prizes(field)

        if score == 2:
            print_field(field, player_x, player_y)
            print("Поздравляем! Все призы собраны!")
            print("Вы выиграли!")
            game_over = True

        elif old_x == player_x and old_y == player_y:
            print("Движение невозможно!")

    print("\nИтоговый счет:", score)
    print("Количество ходов:", moves)


if __name__ == "__main__":
    main()
