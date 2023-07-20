# Standard modules can be found here: https://docs.python.org/3/py-modindex.html

user_choice = input("Which exercise?\n")

match user_choice:
    # Exercise 1
    case '1':
        import glob
        # https://docs.python.org/3/library/glob.html

        myfiles = glob.glob("./exercise6_txt_files/*.txt")

        for filepath in myfiles:
            with open(filepath, 'r') as file:
                print(file.read().upper())


    # Exercise 2
    case '2':
        import csv 

        with open("weather.csv", "r") as file:
            data = list(csv.reader(file))

        print(data)

        city = input('Enter a city: ').title().strip()

        for row in data[1:]:
            if row[0] == city:
                print(row[1])

    # Exercise 3
    case '3':
        import shutil
        
        try:
            shutil.make_archive('output', 'zip', './exercise6_txt_files')
        except: 
            print('Unable to zip folder, makesure you have specified the correct PATH')

        print('Files zipped sucessfully.')


    # Exercise 4
    case '4':
        import webbrowser

        user_search = input('Enter a search term: ').replace(" ","+")
        webbrowser.open("https://www.google.com/search?q="+ user_search)