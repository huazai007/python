total = 0

sum_number = 0
while True:
	number_input = raw_input('number: ')
	if not number_input:
		break
	else:
		sum_number = sum_number + int(number_input)
		total = total + 1.0
		avg_number = sum_number/total 	
print avg_number
