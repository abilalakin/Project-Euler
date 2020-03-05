def isPrime(n):
    if n % 2 == 0:
        return False

    i = 3
    while i < n**0.5+1:
        if n % i == 0:
            return False
        i += 2
    return True

def nthPrime(n):
    prime = 2
    count = 1
    curr = 3

    while count < n:
        if isPrime(curr):
            count += 1
        curr += 2
        
    return curr-2        

                