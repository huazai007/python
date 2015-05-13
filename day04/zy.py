log= {}           
f=open('/home/share/www_access_20140823.log')
for i in f.read().split('\n'):
	arr=i.split(' ')
	if arr[0] !="":
		tmp_lst=arr[8],arr[6],arr[0]
		if tmp_lst not in log:
			log[tmp_lst]=1
		else:
			log[tmp_lst]=log[tmp_lst]+1
for (k,v) in log.items():
	s=(k[2],v)
	item=[k[0],k[1],s]
	print item
