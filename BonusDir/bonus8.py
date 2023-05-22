filenames = ['1.doc','1.report','1.presentation']
new_filenames = []

# for file in filenames:
#     file = file.replace('.','-')
#     file = file + '.txt'
#     new_filenames.append(file)
# print(new_filenames)

filenames = [file.replace('.','-')+'.txt' for file in filenames]
print(filenames)

new = [i for i in ['a', 'b']]
print(new)