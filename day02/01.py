arr = [1,2,3,4,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
init_v = False
for i in arr:
	if i == 2:
		init_v = True
		break
print "%d is %s" %(i,init_v)
