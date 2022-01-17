# algorithm-generator
Generate algorithms and search a working algorithm for your puzzle.

See algorithm_generator.py how the algorithm generator works.

You can test to find an algorithm for your problem:

```python
python3 -m pip install sympy
```

```python
from algorithm_generator import test_algorithms

tested_algorithm_list = []

false_prime_list = [22, 25, 27, 30, 35, 49, 77]
true_prime_list = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

test_list = []
for value in false_prime_list:
    test_list.append((value, False))
for value in true_prime_list:
    test_list.append((value, True))

while True:
  # True example list, False example list, list of tested algorithms, complexity (how many AND/OR parts)
  working_algorithm = test_algorithms(test_list, tested_algorithm_list, complexity=2)
  if working_algorithm:
    print(working_algorithm)
```

Example code searches isPrime algorithms:

```sh
python create_isPrime_algorithms.py
```
