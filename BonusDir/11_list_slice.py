def get_average():
    with open('files/data.txt', 'r') as file:
        data = file.readlines()

    total_num = 0
    values = data[1:]
    # values = [float(i[:-1]) for i in values]
    # sum(values)

    for val in data[1:]:
        temp_value = float(val[:-1])
        total_num += temp_value
        print(val)
    
    average_temp_local = total_num / len(data[1:])
    return average_temp_local


average = get_average()
print(average)