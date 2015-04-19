arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i>=0 and arr[i] > key:
                arr[i+1] = arr[i]
                i = i-1
        arr[i+1] =key
print arr
