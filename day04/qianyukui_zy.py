log_file = open('www_access_20140823.log')
#statistics
dict_log = {}
while True:
    line = log_file.readline()
    try:
        if line != '\n' and line != '':
            temp_tuple = (line.split()[0],line.split()[6],line.split()[8])
            dict_log[temp_tuple] = dict_log.get(temp_tuple,0) + 1
        elif line == '':
            break
    except:
        print line
#covert dict to list
sort_list = []
for (k,v) in dict_log.items():
    sort_list.append((k,v))
#sort
i = 0
while i <= 9 or sort_list[i-1][1] == sort_list[i-2][1]:
    for j in range(i,len(sort_list)):
        if sort_list[i][1] < sort_list[j][1]:
            sort_list[i],sort_list[j] = sort_list[j],sort_list[i]
    i += 1
#print result
rank = 1
print_string = 'No.%s: From %s to %s status %s is %s.'
for j in range(i-1):
    if sort_list[j][1] == sort_list[j-1][1]:
        print print_string % ((rank,)+sort_list[j][0]+(sort_list[j][1],))
    else:
        print print_string % ((j+1,)+sort_list[j][0]+(sort_list[j][1],))
        rank = j+1

