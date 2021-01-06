from functools import reduce

# 1) Using functional programming constructs (lambda): create function that calculates Fibonacci sequence for given N:
#       Fib(0) == 0
#       Fib(1) == 1
#       Fib(N) == Fib(N-1) + Fib(N-2) || (N > 1)

silnia = lambda n: reduce(lambda a, b: a * b, range(1, n+1))
print(silnia(5))
def silnia_rek(n):
    if n <= 1:
        return 1
    else:
        return n * silnia_rek(n-1)


print(f"Rekurencyjnie: {silnia_rek(5)}")


fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fib(1))


# 2) Create a function calculating sum for any number of integers given to that function as arguments
#    (don't use built-in function sum).


def calc_sum(list_of_ints):
    return reduce(lambda a, b: a + b, list_of_ints)
print(calc_sum([1,2,3,4,5,6,7,8,9]))

# 3) Create a function, which takes range and returns list of
#    square of odd integers from given range (do not use loops)
#    Don't use loops (neither for nor while). List comprehensions are allowed.

def odd_int_squares(start, stop):
    return [num**2 for num in range(start, stop) if num % 2 != 0]


print(odd_int_squares(1, 19))

# 4) Create a function, which takes strings list and returns only those strings which start from letter "b".
#    Don't use loops (neither for nor while). List comprehensions are allowed.
#    Check this function on file three_rings.txt.

# 5) Create a function, which takes strings list and exchanges
#    any letter "o" into "."
#    Don't use loops (neither for nor while). List comprehensions are allowed.
#    Check this function on file three_rings.txt.
