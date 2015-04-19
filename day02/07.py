arr = []
while True:

	input = raw_input('input: ')
	if input == 'add':
		detail = raw_input('detail.......:')
		arr.append(detail)
		print arr
	elif input == 'do':
		if len(arr) ==0:
			break
		print arr.pop(0)
