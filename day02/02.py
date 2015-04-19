arr = [1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
len = 0
max = 0
min = 1
for i in arr:
	len = len+1
	if i > max:
		max =i
	if i < min:
		min =i
print "len is %d" %(len)
print "max is %d" %(max)
print "min is %d" %(min)
