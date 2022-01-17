''' Generate and test algorithms '''
import random
import sympy

def algorithm_generator(tested_algorithm_list, statements=True, variable_count=1):
    ''' Returns an algorithm. Examples:
    0 == 3 ** a % a
    0 < 1 - a ** a
    6 - a * 2 != a
    '''
    comparions = ['==', '>']
    logic = ['*', '-', '+', '%', '**']
    if statements:
        operators =  comparions + logic
    else:
        operators = logic
    numbers = []
    variable_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    #a, b, c, d, e, f, g = sympy.symbols(' '.join(variable_list))
    for index in range(0, variable_count):
        numbers.append(variable_list[index])
    components = []
    for number in numbers:
        element = '(%s - 1)' % number
        components.append(element)
        element = '(%s + 1)' % number
        components.append(element)
        if number != 'a':
            element = '(%s - a)' % number
            components.append(element)
            element = 'abs(%s - a)' % number
            components.append(element)
            element = '((%s - a) * (a - %s))' % (number, number)
            components.append(element)
    numbers = numbers + ['-3', '-2', '-1', '1', '2', '3', '0']
    operation_list = []
    statement_ready = False if statements else True
    number_ready = 0
    next_add_number = True
    while True:
        if not next_add_number:
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

            next_add_number = True

            if random.choice([1, 2, 3, 4]) == 4: # 25% of time add a component
                operation_list.append(random.choice(components))
                next_add_number = False # Next must be operator as well

        else:
            if operation_list:
                if operation_list[-1] == '%' or operation_list[-1] == '(':
                    number = random.choice(numbers[0:-1]) # Without zero!
            else:
                number = random.choice(numbers)

            operation_list.append(number) # Append a number
            next_add_number = False

            if number in variable_list:
                number_ready = number_ready + 1

            if statement_ready and number_ready >= variable_count:
                algo = ' '.join(operation_list)
                #simple_form = sympy.simplify(eval(' '.join(operation_list)))
                #algo = str(simple_form)
                algohash = hash(algo)
                if not algohash in tested_algorithm_list:
                    tested_algorithm_list.append(algohash)
                    return algo

def simplify(expression_string):
    ''' Simplify an expression with simply '''
    variable_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    a, b, c, d, e, f, g = sympy.symbols(' '.join(variable_list))
    comparions = ['==', '>']
    simple_form = sympy.simplify(eval(expression_string))
    return str(simple_form)

def Mod(value1, value2):
    ''' Because sympy wrotes % to Mod() '''
    return value1 % value2

def Abs(value):
    ''' Because sympy wrotes abs() to Abs() '''
    return abs(value)

def algorithm(input, output, algo):
    ''' Execute the algorithm '''
    if isinstance(input, list):
        for index, value in enumerate(input):
            if index == 0:
                a = value
            if index == 1:
                b = value
            if index == 2:
                c = value
            if index == 3:
                d = value
            if index == 4:
                e == value
            if index == 5:
                f == value
            if index == 6:
                g == value
    else:
        a = input
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
