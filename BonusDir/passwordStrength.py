user_password = input('Enter new password: ')
# result = []
result = {}

if len(user_password) >= 8:
    result['length'] = True
else:
    result['length'] = True

contains_num = False
for char in user_password:
    if char.isdigit():
        contains_num = True
result['number'] = contains_num

contains_up = False
for char in user_password:
    if char.isupper():
        contains_up = True
result['uppercase'] = contains_up

print(result)
print(result.values())
print(result.keys())
# print(all(result))

if all(result.values()):
    print('Strong Password!')
else:
    print('Weak Password...')