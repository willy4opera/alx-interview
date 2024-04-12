#!/usr/bin/python3

'''The N queens solution finder module.
'''
import sys


d_solution = []
'''Declare a list of possible solutions to the N queens problem.
'''
num = 0
'''Here, we declare initial size of the chessboard.
'''
ls_pos = None
'''List of possible positions on the chessboard.
'''


def fetch_input():
    '''Here, we retrieved and validated the program's argument.

    Returns:
        int: The size of the chessboard.
    '''
    global num
    num = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if num < 4:
        print("N must be at least 4")
        sys.exit(1)
    return num


def attacking(ls_pos0, ls_pos1):
    '''Here, we check if the positions of two queens are in an attacking mode.

    Args:
        ls_pos0 (list or tuple): The first queen's position.
        ls_pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    '''
    if (ls_pos0[0] == ls_pos1[0]) or (ls_pos0[1] == ls_pos1[1]):
        return True
    return abs(ls_pos0[0] - ls_pos1[0]) == abs(ls_pos0[1] - ls_pos1[1])


def check_group(group):
    '''Here, we checks that a group exists in the list of solutions.

    Args:
        group (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    '''
    global d_solution
    for stn in d_solution:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == num:
            return True
    return False


def dev_solution(row, group):
    '''Here, we builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    '''
    global d_solution
    global num
    if row == num:
        tmp0 = group.copy()
        if not check_group(tmp0):
            d_solution.append(tmp0)
    else:
        for col in range(num):
            a = (row * num) + col
            fnd_match = zip(list([ls_pos[a]]) * len(group), group)
            founf_position = map(lambda x: attacking(x[0], x[1]), fnd_match)
            group.append(ls_pos[a].copy())
            if not any(founf_position):
                dev_solution(row + 1, group)
            group.pop(len(group) - 1)


def fetch_solution():
    '''Here, we gets the solutions for the given chessboard size.
    '''
    global ls_pos, num
    ls_pos = list(map(lambda x: [x // num, x % num], range(num ** 2)))
    a = 0
    group = []
    dev_solution(a, group)


num = fetch_input()
fetch_solution()
for solution in d_solution:
    print(solution)
