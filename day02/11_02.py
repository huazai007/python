arr = [1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
for i in range(1,len(arr)):
	j = i -1
	while j >=0 and arr[i] <arr[j]:
		arr[j+1]=arr[j]
		j=j-1
print arr
