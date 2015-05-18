def hello(name,*params):
	print "name is %s "%name
	sum = 0
	for i in params:
		sum=sum+i
	print "money is sum"
hello('huazai',1,2,3,4,5)
