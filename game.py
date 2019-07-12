# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:

import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 16))
    field.append(EMPTY_MARK)
    for i in range(100):
        random_key = random.choice(list(MOVES))
        try:
            field = perform_move(field, random_key)
        except IndexError:
            continue

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16, 4):
        for j in range(i, i + 4):
            if len(str(field[j])) == 1:
                print(field[j], end='  ')
            else:
                print(field[j], end=' ')
        print()


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    finished_field = list(range(1, 16))
    finished_field.append(EMPTY_MARK)
    return field == finished_field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """

    old_pos = field.index(EMPTY_MARK)
    new_pos = old_pos + MOVES[key]
    if key == 'w' and old_pos < 4:
        raise IndexError('Движение вверх невозможно')
    if key == 'a' and old_pos % 4 == 0:
        raise IndexError('Движение влево невозможно')
    if key == 's' and old_pos > 11:
        raise IndexError('Движение вниз невозможно')
    if key == 'd' and old_pos % 4 == 3:
        raise IndexError('Движение вправо невозможно')
    field[old_pos], field[new_pos] = field[new_pos], field[old_pos]

    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """
    while True:
        user_input = input('Сделайте ход: w,a,s,d: ')
        if user_input in MOVES.keys():
            return user_input


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """

    field = shuffle_field()
    print_field(field)
    move_counter = 0
    while not is_game_finished(field):
        try:
            key = handle_user_input()
            field = perform_move(field, key)
            move_counter += 1
        except IndexError as e:
            print(e)
        except KeyboardInterrupt:
            print('shutting down')
            break
        finally:
            print_field(field)
    print('Сделано ходов: ', move_counter)


if __name__ == '__main__':
    main()
