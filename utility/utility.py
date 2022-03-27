from pydoc import doc
import random

def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
        https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = random.getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

def is_generator(n: int, p: int) -> bool:
    """Algorithm given in the assignment"""
    if not is_prime(p):
        raise ValueError("The second argument is not a prime number")
    if n >= p:
        return False
    pfs = prime_factors(p - 1)
    for q in pfs:
        r = (n ** ((p-1) / q)) % p
        if r == 1:
            return False
    return True

def prime_factors(n: int):
    """Source: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/"""
    l = []
    c = 2
    while(n > 1):
        if(n % c == 0):
            l.append(c)
            n = n / c
        else:
            c = c + 1
    return l
