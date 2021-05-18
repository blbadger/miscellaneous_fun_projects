# factorial_zeros.py

def is_prime(number):
    '''Determines if the argument number is prime.
    Outputs True if prime, else False.
    '''
    if number == 2:
        return True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_digits(base, n):
    '''A helper function that adds the digits 
    of the argument n in the base provided.
    '''
    number_ls = []

    while n >= base:
        remainder = n % base
        number_ls.append(remainder)
        n -= remainder
        n = int(n // base)
    number_ls.append(n)
    return sum(number_ls)

def zeros(base, n):
    '''Returns the number of 0s trailing the factorial of a number (n) supplied in any given base (argument base)
    using Legendre's method.  This allows for the numer of trailing zeros to be computed for inputs whose factorial
    is not computable in any reasonable amount of time.
    '''

    # Import standard library
    import math

    exponent = 1
    ls = []
    if not is_prime(base):
        for i in range(2, base//2 + 1):
            if is_prime(i) and base%i == 0:
                j = 1
                while base % (i ** j) == 0:
                    j += 1
                exponent = j - 1
                ls.append([i, exponent])
    else:
        ls.append([base, 1])
    
    # Legendre's method for computing trailing zeros 
    power_ls = []
    for pair in ls:
        power = int((n-sum_digits(pair[0], n))/(pair[0] - 1))
        power_ls.append(power // pair[1])

    if not power_ls: return 0
    return min(power_ls)

# example inputs
base = 101
n = 458485842345723948572385732094875239847

# example function call
print (zeros(base, n))

