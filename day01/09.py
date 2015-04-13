list = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
result = {}
for key in list:
	if  key in result:
		result[key] = result[key] + 1
	else:
		result[key] = 1
print result
for s in result:
	print '%s num is %s' % (s,result[s]) 
