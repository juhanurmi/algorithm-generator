''' Search factorization algorithm '''
import time
from algorithm_generator import test_algorithms, simplify

tested_algorithm_list = []
working_algorithm_list = []

def gcd(a, b):
    '''
    The most simple form of Euclid's method for computing the greatest common divisor.
    Two positive integers consists of replacing the larger number by the difference of the numbers,
    and repeating this until the two numbers are equal: that is their greatest common divisor.
    This method is slow and mainly just reminder here how to create a working algorithm.
    '''
    if a == b:
        return b
    if a > b:
        a = a - b
    else:
        b = b - a
    return gcd(a, b)

test_list = []
for numbers in [[6, 2], [44, 33], [125, 25], [49, 14], [213, 142], [169, 39]]:
    test_list.append((numbers, gcd(numbers[0], numbers[1])))

try:
    print('Quit the search by pressing ctrl+c (SIGINT)')
    start_time = time.time()
    while True:
        if tested_algorithm_list and len(tested_algorithm_list) % 10000 == 0:
            print('Testing %d algorithms per second.' % int(10000/(time.time() - start_time)))
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
