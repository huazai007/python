list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max = 0
max_second = 0
for i in list:
	if i > max:
		max_second = max
		max =i
	elif  max > i > max_second:
		max_second = i
print max 
print max_second 
