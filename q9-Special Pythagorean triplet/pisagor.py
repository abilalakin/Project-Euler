def pisa():
	for a in range(1,998):
		for b in range(a+1,998):
			c = 1000 -a -b
			if c*c == a*a + b*b:
				print(a)
				print(b)
				print(c)
				return a*b*c 


print(pisa())				