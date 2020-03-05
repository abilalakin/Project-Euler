lst = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def evenDiv():
	for i in range(2520,999999999,2520):
		if all(i % num == 0 for num in lst):
			return i