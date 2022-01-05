''' Generate and test algorithms '''
import random

def algorithm_generator(tested_algorithm_list, statements=True):
    ''' Returns an algorithm. Examples:
    0 == 3 ** number % number
    0 < 1 - number ** number
    6 - number * 2 != number
    '''
    comparions = ['==', '>']
    logic = ['*', '-', '+', '%', '**']
    if statements:
        operators =  comparions + logic
    else:
        operators = logic
    numbers = ['number', '0.5', '-3', '-2', '-1', '1', '2', '3', '4', '5', '0']
    operation_list = []
    statement_ready = False if statements else True
    number_ready = False
    index = 0
    while True:
        index = index + 1
        if index % 2 == 0:
            if operation_list[-1] == '0' and operators[-1] == '**':
                operator = random.choice(operators[0:-1])
            else:
                operator = random.choice(operators)

            operation_list.append(operator) # Append operator

            if not statement_ready and operator in comparions:
                statement_ready = True # This is now a ready to test
                for comp in comparions:
                    operators.remove(comp)
            if operator == '**': # Use ** only once
                operators.remove(operator)
        else:
            if operation_list and operation_list[-1] == '%':
                number = random.choice(numbers[0:-1]) # Without zero!
            else:
                number = random.choice(numbers)

            operation_list.append(number) # Append a number

            if not number_ready and number == 'number':
                number_ready = True
            if statement_ready and number_ready:
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

def test_algorithms(test_list, tested_algorithm_list, complexity=1, statements=True):
    ''' Test algorithm with true and false samples '''
    algo = ''
    for index in range(1, complexity + 1):
        if index == 1:
            part_algo = algorithm_generator(tested_algorithm_list, statements)
            algo = '(' + part_algo + ')'
        else:
            part_algo = algorithm_generator(tested_algorithm_list, statements)
            algo = algo + random.choice([' and ', ' or ']) + '(' + part_algo + ')'
    for test in test_list:
        number = test[0]
        value = test[1]
        if algorithm(number, algo) != value:
            return False
    return algo # Found a working algorithm against the test data
