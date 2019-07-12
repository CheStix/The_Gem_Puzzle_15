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
        old_pos = field.index(EMPTY_MARK)
        new_pos = old_pos + MOVES[random.choice(['w', 'a', 's', 'd'])]
        try:
            field[old_pos], field[new_pos] = field[new_pos], field[old_pos]
        except IndexError:
            pass

    return field
    pass


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
    if key == 'w' and old_pos in (0, 1, 2, 3):
        raise IndexError
    if key == 'a' and old_pos in (0, 4, 8, 12):
        raise IndexError
    if key == 's' and old_pos in (12, 13, 14, 15):
        raise IndexError
    if key == 'd' and old_pos in (3, 7, 11, 15):
        raise IndexError
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
        if user_input in ('w', 'a', 's', 'd'):
            return user_input
    pass


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
        except IndexError:
            print('Ход не возможен')
        except KeyboardInterrupt:
            print('shutting down')
            break
        finally:
            print_field(field)
    print('Сделано ходов: ', move_counter)


if __name__ == '__main__':
    main()
