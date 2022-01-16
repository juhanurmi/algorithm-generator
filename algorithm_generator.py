''' Generate and test algorithms '''
import random

def algorithm_generator(tested_algorithm_list, statements=True, variable_count=1):
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
    numbers = []
    for index in range(0, variable_count):
        if index == 0:
            numbers.append('number')
        else:
            numbers.append('number' + str(index))
    numbers = numbers + ['-3', '-2', '-1', '1', '2', '3', '0']
    operation_list = []
    statement_ready = False if statements else True
    number_ready = False
    closed_brackets = True
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

            if closed_brackets and random.choice([True, False]):
                operation_list.append('(')
                closed_brackets = False

        else:
            if operation_list:
                if operation_list[-1] == '%' or operation_list[-1] == '(':
                    number = random.choice(numbers[0:-1]) # Without zero!
            else:
                number = random.choice(numbers)

            operation_list.append(number) # Append a number

            if not number_ready and number == 'number':
                number_ready = True

            if not closed_brackets:
                operation_list.append(')')
                closed_brackets = True

            if statement_ready and number_ready and closed_brackets:
                algo = ' '.join(operation_list)
                algohash = hash(algo)
                if not algohash in tested_algorithm_list:
                    tested_algorithm_list.append(algohash)
                    return algo

def algorithm(input, output, algo):
    ''' Execute the algorithm '''
    if isinstance(input, list):
        for index, value in enumerate(input):
            if index == 0:
                number = value
            else:
                vars()['number' + str(index)] = value
    else:
        number = input
    try:
        return eval(algo) == output
    except Exception as error:
        print(input, algo, error)
        return False

def test_algorithms(test_list, tested_algorithm_list, complexity=1, statements=True):
    ''' Test algorithm with true and false samples '''
    if isinstance(test_list[0][0], list):
        variable_count = len(test_list[0][0])
    else:
        variable_count = 1
    algo = ''
    for index in range(1, complexity + 1):
        if index == 1:
            part_algo = algorithm_generator(tested_algorithm_list, statements, variable_count)
            algo = '(' + part_algo + ')'
        else:
            part_algo = algorithm_generator(tested_algorithm_list, statements, variable_count)
            algo = algo + random.choice([' and ', ' or ']) + '(' + part_algo + ')'
    for test in test_list:
        input = test[0]
        output = test[1]
        if not algorithm(input, output, algo):
            return False
    return algo # Found a working algorithm against the test data
