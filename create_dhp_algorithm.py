''' Search algorithm for Diffie-Hellman problem:
Given an element g and the values of g**x and g**y, what is the value of g**xy.
'''
import time
from math import sqrt, ceil
from algorithm_generator import test_algorithms, simplify

tested_algorithm_list = []
working_algorithm_list = []

def xfromgx(g, gx):
    '''
    Input is g and g**x.
    Slow solver for x.
    '''
    exponent = 0
    while True:
        exponent = exponent + 1
        if g**exponent == gx:
            return exponent

def gxy(g, gx, gy):
    '''
    Input is g, g**x and g**y.
    Slow solver for g**xy.
    '''
    exponent = 0
    x = 0
    y = 0
    while True:
        exponent = exponent + 1
        test = g**exponent
        if test == gx:
            x = exponent
        elif test == gy:
            y = exponent
        if x != 0 and y != 0:
            return g**(x*y)

test_list = []
for numbers in [[5, 125, 3125], [3, 243, 59049], [33, 39135393, 42618442977], [8, 134217728, 8589934592], [3, 14348907, 10460353203], [6, 2176782336, 13060694016]]:
    test_list.append((numbers, gxy(numbers[0], numbers[1], numbers[2])))

#test_list = []
#for numbers in [[5, 125], [3, 243], [33, 39135393], [8, 134217728], [3, 14348907], [6, 2176782336]]:
#    test_list.append((numbers, xfromgx(numbers[0], numbers[1])))

try:
    print('Quit the search by pressing ctrl+c (SIGINT)')
    start_time = time.time()
    while True:
        if tested_algorithm_list and len(tested_algorithm_list) % 1000 == 0:
            print('Testing %d algorithms per second.' % int(1000/(time.time() - start_time)))
            print('Tested %d algorithms. %d working algorithms found.' % (len(tested_algorithm_list), len(working_algorithm_list)))
            start_time = time.time()
        working_algorithm = test_algorithms(test_list, tested_algorithm_list, complexity=1, statements=False)
        if working_algorithm:
            simple = simplify(working_algorithm)
            if not simple in working_algorithm_list:
                working_algorithm_list.append(simple)
                print('\n%s\n' % simple)
except KeyboardInterrupt:
    pass

if working_algorithm_list:
    print('\nPrint the results:\n')
    for working_algorithm in working_algorithm_list:
        print(working_algorithm + '\n')
