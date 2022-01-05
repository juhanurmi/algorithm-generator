''' Generate and test algorithms '''
import random

def algorithm_generator(tested_algorithm_list):
    ''' Returns an algorithm. Examples:
    0 == 3 ** number % number
    0 < 1 - number ** number
    6 - number * 2 != number
    '''
    comparions = ['==', '!=', '<', '>']
    operators = ['*', '-', '+', '%'] + comparions + ['**']
    numbers = ['number', '-3', '-2', '-1', '1', '2', '3', '0']
    operation_list = []
    ready = False
    index = 0
    while True:
        index = index + 1
        if index % 2 == 0:
            if operation_list[-1] == '0' and operators[-1] == '**':
                operator = random.choice(operators[0:-1])
            else:
                operator = random.choice(operators)
            operation_list.append(operator) # Append operator
            if operator in comparions:
                # Remove all the comparisons from the operators
                for statement in comparions:
                    operators.remove(statement)
                ready = True # This is now a ready to test
            if operator == '**': # Use ** only once
                operators.remove(operator)
        else:
            if operation_list and operation_list[-1] == '%':
                number = random.choice(numbers[0:-1]) # Without zero!
            else:
                number = random.choice(numbers)
            operation_list.append(number) # Append a number
            if ready and 'number' in operation_list and random.choice([True, False]):
                algo = ' '.join(operation_list)
                if not algo in tested_algorithm_list:
                    tested_algorithm_list.append(algo)
                    return algo

def algorithm(number, algo):
    ''' Execute the algorithm '''
    try:
        return eval(algo)
    except Exception as error:
        print(number, algo, error)
        return False

def test_algorithms(true_list, false_list, tested_algorithm_list, complexity=1):
    ''' Test algorithm with true and false samples '''
    algo = ''
    for index in range(1, complexity + 1):
        if index == 1:
            part_algo = algorithm_generator(tested_algorithm_list)
            algo = '(' + part_algo + ')'
        else:
            part_algo = algorithm_generator(tested_algorithm_list)
            algo = algo + random.choice([' and ', ' or ']) + '(' + part_algo + ')'
    for number in true_list: # All these should return True
        if not algorithm(number, algo):
            return False
    for number in false_list: # All these should return False
        if algorithm(number, algo):
            return False
    return algo # Found a working algorithm against the test data
