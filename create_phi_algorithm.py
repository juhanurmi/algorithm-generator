''' Search algorithm to calculate phi '''
import time
from algorithm_generator import test_algorithms, simplify

tested_algorithm_list = []
working_algorithm_list = []

def gcd(a, b):
    ''' Calculate the Greatest Common Divisor of a and b. '''
    if b == 0:
        return a
    return gcd(b, a % b)

def phi(n):
    '''
    For example, the totatives of n = 9 are the six numbers 1, 2, 4, 5, 7 and 8.
    They are all relatively prime to 9.
    gcd(9, 1) = 1
    gcd(9, 2) = 1
    gcd(9, 4) = 1
    gcd(9, 5) = 1
    gcd(9, 7) = 1
    gcd(9, 8) = 1
    The other three numbers 3, 6, and 9 are not.
    gcd(9, 3) = 3
    gcd(9, 6) = 3
    gcd(9, 9) = 9.
    Result is phi(9) = 6.
    '''
    relatively_primes = 0
    for number in range(1, n + 1): # Numbers 1-n
        if gcd(n, number) == 1:
            relatively_primes = relatively_primes + 1
    return relatively_primes

test_list = []
for number in [6, 9, 24, 41, 87]:
    test_list.append((number, phi(number)))

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
