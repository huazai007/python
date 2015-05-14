log= {}           
f=open('/home/share/www_access_20140823.log')
result=[]
for i in f.read().split('\n'):
	arr=i.split(' ')
	if arr[0] !="":
		tmp=arr[8],arr[6],arr[0]
		if tmp not in log:
			log[tmp]=1
		else:
			log[tmp]=log[tmp]+1
for (k,v) in log.items():
	s=(k[2],v)
	tmp_result=[k[0],k[1],s]
	#print result
	result.append(tmp_result)
for line in result:
	outf=open('output.txt','a')
	try:
		outf.writelines(str(line)+'\n')
	finally:
		outf.close()
