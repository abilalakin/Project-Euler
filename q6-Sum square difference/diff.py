def square(x):
	return x*x


sumSquare = sum([square(i) for i in range(1,101)])

squareSum = square(sum([x for x in range(1,101)]))

result = squareSum - sumSquare

print (result)