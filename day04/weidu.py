f=open('tem.txt')
tem_list=[]
for i in f.read().split('\n'):
	arr = i.split(' ')
	print arr
	if len(arr) == 2:
		tem_list.append(float(arr[1]))
print max(tem_list)
total =0
for num in tem_list:
	total= total+num
print total/len(tem_list)
