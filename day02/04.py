arr = [1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
for j in range(len(arr)):
	for i in range(len(arr)-1):
		if arr[i] >arr[i+1]:
			arr[i],arr[i+1] = arr[i+1],arr[i]
print arr
