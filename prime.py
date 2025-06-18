"""
prime.py -- Write the application code here
Devon Singh
"""
#This code will be used to return an integer for the purposes of test_prime.py
def generate_prime_factors(number):
    if type(number) is not int:
        raise ValueError("Please only use Integers")

    if number <= 1:
        return []

    result = []

    def divide_out(n, factor):
        while n % factor == 0:
            result.append(factor)
            n //= factor
        return n

    current = number
    factor = 2

    while factor * factor <= current:
        current = divide_out(current, factor)
        factor += 1

    if current > 1:
        result.append(current)

    return result


