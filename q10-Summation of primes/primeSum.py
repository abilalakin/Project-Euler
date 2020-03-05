def isPrime(n):
    if n % 2 == 0:
        return False

    i = 3
    while i < n**0.5+1:
        if n % i == 0:
            return False
        i += 2
    return True

def sumPrime():
	total = 2
	for i in range(3,2000000,2):
		print (i)
		if isPrime(i):
			total += i
	return total
	
#print(sumPrime())			