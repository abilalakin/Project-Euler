def fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print ("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2,n):
			c = a + b
			a = b
			b = c
		return b
		
def result(): 
	i = 1
	evenList = []
	while fibonacci(i) < 4000000:
		n = fibonacci(i)
		if n % 2 == 0:
			evenList.append(n)
		i += 1	

	print(sum(evenList))			

