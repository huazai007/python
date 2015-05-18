g=lambda x:x*3
print g(3)
g1=lambda x,y:x*y
print g1(3,4)
def demo(func,num1,num2):
	print  func(num1,num2)
demo(lambda x,y:x*y,2,3)
