s = 'aa;bb,ccc;ee,ee;ff,gg;ee'
new_lst=s.replace(';',':').split(',')
d = {}
print new_lst
for i in new_lst:
	print i
	tmp_arr =i.split(':')
	print tmp_arr
	d[tmp_arr[0]] = tmp_arr[1]
print d.items()
