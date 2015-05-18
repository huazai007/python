l=[(404,'xx/xx','19.168',10),(404,'xx/xx','19.168',50),(404,'xx/xx','19.168',3),(404,'xx/xx','19.168',5),(404,'xx/xx','19.168',11)]
#(形势参数)
def sort_fun(arr):
	return arr[3]
for i in sorted(l,key=sort_fun):
	print i
	
