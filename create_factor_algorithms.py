''' Search factorization algorithm '''
import time
from algorithm_generator import test_algorithms

tested_algorithm_list = []
working_algorithm_list = []

test_list = [(4, 2), (9, 3), (25, 5), (49, 7), (121, 11), (169, 13), (213, 71)]

try:
    print('Quit the search by pressing ctrl+c (SIGINT)')
    test_count = 0
    start_time = time.time()
    while True:
        test_count = test_count + 1
        if test_count % 10000 == 0:
            print('Testing %d algorithms per second.' % int(10000/(time.time() - start_time)))
            print('Tested %d algorithms. %d working algorithms found.' % (test_count, len(working_algorithm_list)))
            start_time = time.time()
        working_algorithm = test_algorithms(test_list, tested_algorithm_list, complexity=1, statements=False)
        if working_algorithm:
            working_algorithm_list.append(working_algorithm)
            print(working_algorithm + '\n')
except KeyboardInterrupt:
    pass

if working_algorithm_list:
    print('\nPrint the results:\n')
    for working_algorithm in working_algorithm_list:
        print(working_algorithm + '\n')
