''' Search algorithm for discrete logarithm problem '''
import time
from math import sqrt, ceil
from algorithm_generator import test_algorithms, simplify

tested_algorithm_list = []
working_algorithm_list = []

def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    Example: bsgs(5, 20, 53)) # 11, because 20 = 5**11 % 53
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None

test_list = []
for numbers in [[5, 20, 53], [3, 4, 11], [33, 16, 17], [8, 9, 47], [3, 12, 17], [6, 38, 53]]:
    test_list.append((numbers, bsgs(numbers[0], numbers[1], numbers[2])))

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
