# Advent of Code
#
# Day 4
# 
# Play bingo with a giant squid

import numpy as np

def load_data(filename):
    with open(filename, 'r') as f:
        raw_input = f.read().split('\n\n')

    numbers_string = raw_input[0].strip().split(',')
    numbers = [int(i) for i in numbers_string]

    boards_strings = raw_input[1:]
    boards_strings = [board.strip().split('\n') for board in boards_strings]
    boards_strings = [[row.strip().split() for row in board] \
                        for board in boards_strings]
    boards = np.array(boards_strings, dtype='int')
    board_marks = np.zeros_like(boards)

    return numbers, boards, board_marks


def check_board(board, board_marks):
    ''' Returns true if the board is a winner '''
    rows = board.shape[0]
    cols = board.shape[1]
    winner = np.ones_like(board[0,:])
    win = False

    for column in range(cols):
        if np.array_equal(board_marks[:,column], winner.T):
            return True

    for row in range(rows):
        if np.array_equal(board_marks[row,:], winner):
            return True

    return win


def mark_boards(boards, board_marks, number):
    ''' Mark the boards if they contain the given number '''
    rows = boards[0].shape[0]
    cols = boards[0].shape[1]
    board_marks[np.nonzero(boards == number)] = 1


def squid_bingo(numbers, boards, board_marks):
    ''' Returns the winning board and its marks '''
    winning_board = None
    winning_marks = None
    min_final_round = 5

    round = 0
    while winning_board is None and round < len(numbers):
        number_drawn = numbers[round]
        mark_boards(boards, board_marks, number_drawn)
        if round >= min_final_round:
            for i, board in enumerate(boards):
                if check_board(board, board_marks[i]):
                    winning_board = board
                    winning_marks = board_marks[i]
                    last_called = number_drawn
                    break

        round += 1

    return winning_board, winning_marks, last_called


def compute_last(numbers, boards, board_marks):
    ''' Compute which board will be last to win '''
    board_list = [i for i in range(len(boards))]
    min_final_round = 5
    last_board = None
    last_marks = None

    round = 0
    while len(board_list) > 0 and round < len(numbers):
        number_drawn = numbers[round]
        mark_boards(boards, board_marks, number_drawn)
        if round >= min_final_round:
            boards_remaining = board_list.copy()
            for i in boards_remaining:
                if check_board(boards[i], board_marks[i]):
                    last_board = boards[i]
                    last_marks = board_marks[i]
                    last_called = number_drawn
                    board_list.remove(i)

        round += 1

    return last_board, last_marks, last_called


def compute_score(board, marks, last_called):
    unmarked_sum = np.sum(board[np.nonzero(marks == 0)])
    return unmarked_sum * last_called


if __name__ == '__main__':
    numbers, boards, board_marks = load_data('input.txt')

    # Part A 
    ##winning_board, winning_marks, last_called = \
    ##    squid_bingo(numbers, boards, board_marks)
    ##score = compute_score(winning_board, winning_marks, last_called)
    ##print(score)

    # Part B
    last_board, last_marks, last_called = \
        compute_last(numbers, boards, board_marks)
    last_board_score = compute_score(last_board, last_marks, last_called)
    print(last_board_score)