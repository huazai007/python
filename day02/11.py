array = [14,3,21,2,2,3,4111,22,3333,4]
for i in range(1, len(array)): 
	key = array[i] 
	print key
	j = i - 1 
	while j >= 0 and key < array[j]: 
		array[j + 1] = array[j] 
		array[j] = key 
		j-=1
print array
