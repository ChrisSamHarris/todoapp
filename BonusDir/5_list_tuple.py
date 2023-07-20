user_choice = input('Which exercise? ')

match user_choice:
        case '1':
# tuples | immutability 
            filenames = ['1.RawData.txt', '2.Reports.txt', '3.Presentations.txt']
            num = 0

            for fn in filenames:
                new_fn = fn.replace('.','-', 1)
                # only change the first occurance of the '.'
                filenames[num] = new_fn
                num += 1
                print(new_fn)
            print(filenames)

#################################################################
        case '2':
            print('Tuples example - THIS WILL FAIL')
            tuple_filenames = ('1.RawData.txt', '2.Reports.txt', '3.Presentations.txt')
            # tuples are immutable so as such cant be modified change - highlighted with '()'
            tuple_num = 0 

            for fn in tuple_filenames:
                new_fn = fn.replace('.','-', 1)
                # only change the first occurance of the '.'
                tuple_filenames[tuple_num] = new_fn
                print(new_fn)
                tuple_num += 1
            print(tuple_filenames)
