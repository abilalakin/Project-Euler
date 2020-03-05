def isPalindrome (pal):
	return str(pal) == str(pal)[::-1]

def largest ():
	maxPal = 999999
	minPal = 100000
	print ("abc")
	for i in range(maxPal,minPal,-1): 
		if isPalindrome(i):
			#print (i)
			for j in range(100,1000):
				if i % j == 0:
					div = int(i / j)
					if len(str(div)) == 3:
						#print (i)
						return i