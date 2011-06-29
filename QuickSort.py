def sort(list):
	if len(list) <= 1:
		return list
	smallerList = []
	largerList = []
	pivot = list[0]
	for c in range(1, len(list)):#en(list)):
		if list[c] <= pivot:
			smallerList.append(list[c])
		else:
			largerList.append(list[c])
	return (sort(smallerList) + [pivot] + sort(largerList)) 
