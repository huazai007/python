arr = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = []
for i in arr:
	if i not in arr2:
		arr2.append(i)
print arr2
