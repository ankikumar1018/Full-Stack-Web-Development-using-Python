tup = (('a', 21), ('b', 37), ('c', 11), ('d', 29))
tup = list(tup)
def Sort_Tuple(tup):
	
	lst = len(tup)
	for i in range(0, lst):
		
		for j in range(0, lst-i-1):
			if (tup[j][1] > tup[j + 1][1]):
				temp = tup[j]
				tup[j]= tup[j + 1]
				tup[j + 1]= temp
	return tuple(tup)

	
print(Sort_Tuple(tup))
