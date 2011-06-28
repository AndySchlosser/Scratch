def sort(list=[]):
	if len(list) <= 1:
		return list
	else:
		pass
	smallerList = []
	largerList = []
	pivot = list[0]
	for c in xrange(len(list) + 1):
		if list[c] <= pivot:
			smallerList += list[c]
		else:
			largerList += list[c]
	list = largerList + smallerList
	return list
