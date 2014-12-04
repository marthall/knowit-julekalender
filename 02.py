
def get_primes(upto):
    primes = {2}
    for i in range(2, upto):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
        if is_prime:
            primes.add(i)
    return primes

def is_relevant_prime(x): return x >= 10 and not int(str(x)[0]) % 2 == 0

primes = map(str, filter(is_relevant_prime, get_primes(100)))

N = "9"

correct_solutions = set()

def construct(number, remaining):
    print number
    if len(number) == int(N):
        correct_solutions.add(number)
    for i in remaining:
        if number[-1] == i[0]:
            construct(number + i[1], filter(lambda x: x != i, remaining))

construct(N, primes)

# print correct_solutions
print "Solution: " + min(correct_solutions)
