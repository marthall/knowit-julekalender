import itertools
from math import sqrt

perm_iterator = itertools.imap(lambda x: int("".join(x)), itertools.permutations("123456789"))

min_max_prime_factor = 1000000000

for number in perm_iterator:
    print number, 

    i = 2
    while i * i < number:
        while number % i == 0:
            if i == number:
                break
            number = number / i
        i += 1

    if number < min_max_prime_factor:
        min_max_prime_factor = number
    
    print min_max_prime_factor

print min_max_prime_factor
