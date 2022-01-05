''' Simple way to test isPrime algorithms '''

def isPrime(number, operation):
    '''
    This is a test prime testing algorithm, for example:
    return 0 < 6 - ((3 % (-2 ** number))) % number
    return 0 < 3 - 2 ** number % number
    return -3 % -2 == -1 + 1 % -3 % 2 + 2 % -2 ** number % number - 0 % -3
    return 0 == -2 ** number * -1 % number - 2
    return number == -3 ** number % number + 3
    return 0 == 2 - ((2 ** number) % number)
    return 0 == -3 ** number % number + 3 - number)
    return 0 > ((2 ** number) % number) - 3
    return ((2 ** number) % number) < 0.5 ** number + 2
    return 3 > -0.5 ** number - -0.5 - -0.5 + ((2 ** number) % number) - 0
    return ((2 ** number) % number) < 0.5 ** number + 3 - 1 % number
    '''
    return eval(operation)

def isprime(number):
    ''' This is a working prime number testing algorithm '''
    for index in range(2, int(number**1/2) + 1):
        if number % index == 0:
            return False
    return True

def test_false_positives_and_negatives(operation, count=10000):
    ''' Test numbers from 11 to count '''
    false_negatives = []
    false_positives = []
    for number in range(11, count):
        truth = isprime(number)
        test = isPrime(number, operation)
        if truth and not test:
            false_negatives.append(number)
        if not truth and test:
            false_positives.append(number)
    print('Tests %d' % count)
    print('False negatives %d' % len(false_negatives))
    print(false_negatives[0:20])
    print('False positives %d' % len(false_positives))
    print(false_positives[0:20])

def print_results(operation):
    ''' Print test results '''
    test_false_positives_and_negatives(operation, count=10000)
    row = ''
    multiplier = 12
    for number in range(6, 100):
        if number == multiplier:
            print(row)
            number = ('%d\t' % number) if not isPrime(number, operation) else '\033[92m[%d]\033[00m\t' % number
            row = number
            multiplier = multiplier + 6
        else:
            number = ('%d\t' % number) if not isPrime(number, operation) else '\033[92m[%d]\033[00m\t' % number
            row = row + number

def main():
    ''' Test some examples '''
    algo = '0 == 2 - ((2 ** number) % number)'
    print_results(algo)

if __name__ == "__main__":
    main()
