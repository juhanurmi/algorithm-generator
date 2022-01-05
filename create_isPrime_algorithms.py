''' Search a prime number testing algorithm '''
import time
from algorithm_generator import test_algorithms
from test_prime_algorithms import print_results, test_false_positives_and_negatives

tested_algorithm_list = []
working_algorithm_list = []

false_prime_list = [22, 25, 27, 30, 35, 49, 77]
true_prime_list = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

test_list = []
for value in false_prime_list:
    test_list.append((value, False))
for value in true_prime_list:
    test_list.append((value, True))

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
        working_algorithm = test_algorithms(test_list, tested_algorithm_list, complexity=1)
        if working_algorithm:
            working_algorithm_list.append(working_algorithm)
            print(working_algorithm + '\n')
            test_false_positives_and_negatives(working_algorithm, count=10000)
except KeyboardInterrupt:
    pass

if working_algorithm_list:
    print('\nPrint the results:\n')
    for working_algorithm in working_algorithm_list:
        print(working_algorithm + '\n')
        print_results(working_algorithm)
