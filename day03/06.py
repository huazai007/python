init_d = {'waihao':'pc','name':'pc','a':'pc','age':12,'job':'IT'}
end_d = {}
for (k,v) in init_d.items():
	if v in end_d:
		if type(end_d[v]) != type([]):
			end_d[v] = [end_d[v],k]
		else:end_d[v].append(k)	
	else:end_d[v] = k
print end_d
