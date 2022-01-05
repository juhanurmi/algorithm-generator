''' Search a prime number testing algorithm '''
from algorithm_generator import test_algorithms
from test_prime_algorithms import print_results, test_false_positives_and_negatives

tested_algorithm_list = []
working_algorithm_list = []

#false_prime_list = [16, 32, 64, 128, 256, 341, 512, 561, 645, 1024, 1105, 1387, 1729, 1905, 2047, 2048, 2465, 2701, 2821, 3277, 4033, 4369, 4371, 4681, 5461, 6601, 7957, 8321]
false_prime_list = [22, 25, 27, 30, 35, 49, 77]
true_prime_list = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

try:
    print('Quit the search by pressing ctrl+c (SIGINT)')
    while True:
        working_algorithm = test_algorithms(true_prime_list, false_prime_list, tested_algorithm_list, complexity=2)
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
