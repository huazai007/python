while True:
        year_number = int(raw_input('year: '))
        if year_number%100 == 0 and year_number%400 == 0:
                print '%d is ruiyear' % (year_number)
                break
        elif year_number%4 == 0:   
                print '%d is ruiyear' % (year_number)
                break
        else:
                print ' no ok!!'
