def function(x):
	factors = []
	loop = 2
	while loop <= x:
		if x%loop == 0:
			x/=loop
			factors += [loop]
		else:
			loop += 1
	return factors
