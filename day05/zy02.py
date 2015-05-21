def f(*var):
	s=var
	lst=[]
	for i in list(s[0]):
		lst.append(i)
	result=int(lst.pop(0))
	while len(lst) > 0:
		operator=lst.pop(0)
		if operator == '+':
			result+=int(lst.pop(0))
		elif operator == '-':
			result-=int(lst.pop(0))
	return result
print f('1+2+3-4')
