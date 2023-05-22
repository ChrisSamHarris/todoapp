# tuples | immutability 
filenames = ['1.RawData.txt', '2.Reports.txt', '3.Presentations.txt']
num = 0

for fn in filenames:
    new_fn = fn.replace('.','-', 1)
    # only change the first occurance of the '.'
    filenames[num] = new_fn
    print(new_fn)
    num += 1
print(filenames)

#################################################################

print('Tuples example - THIS WILL FAIL')
tuple_filenames = ('1.RawData.txt', '2.Reports.txt', '3.Presentations.txt')
# tuples are immutable so as such cant be modified change 
tuple_num = 0 

for fn in tuple_filenames:
    new_fn = fn.replace('.','-', 1)
    # only change the first occurance of the '.'
    tuple_filenames[num] = new_fn
    print(new_fn)
    num += 1
print(tuple_filenames)
