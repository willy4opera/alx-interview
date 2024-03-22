#!/usr/bin/python3

'''The python minimum operations coding challenge.
'''


def minOperations(n):
    '''Calculated the least number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    option_c = 0
    clpbd = 0
    completed = 1
    # print('H', end='')
    while completed < n:
        if clpbd == 0:
            # init (the first copy all and paste)
            clpbd = completed
            completed += clpbd
            option_c += 2
            # print('-(11)->{}'.format('H' * completed ), end='')
        elif n - completed > 0 and (n - completed) % completed == 0:
            # copy all and paste
            clpbd = completed
            completed += clpbd
            option_c += 2
            # print('-(11)->{}'.format('H' * completed ), end='')
        elif clpbd > 0:
            # paste
            completed += clpbd
            option_c += 1
            # print('-(01)->{}'.format('H' * completed ), end='')
    # print('')
    return option_c
