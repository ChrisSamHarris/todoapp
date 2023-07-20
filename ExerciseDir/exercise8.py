# A client wants to buy a coin-flip probability program from you.
# The programs should work like this:
# 1. The user runs the program. The program asks the user to enter "head" or "tail".  The user flips a coin and then enters "head" or "tail". 
# The user does the same over and over again.

# In each cycle, the program should return the current percentage of heads in the program. Also, you should write each user entry 
# (i.e., head or tail) in a text file using a with-context manager, one entry per line.

# ===== My Version 1 ==== 
head_count = 0
num_goes = 0

while True:
    user_choice = input('Throw the coin and enter head or tail here: ? ').lower().strip()
    if user_choice == 'q':
        with open('./heads_or_tails/headstails.txt' , 'w') as file:
            file.write(f'')
            # Will refresh the file
        break
    else:
        num_goes += 1
        with open('./heads_or_tails/headstails.txt' , 'a') as file:
            file.write(f'{user_choice}\n')
        if user_choice == 'head':
            head_count += 1
        percentage_heads = (head_count / num_goes) * 100
        print(f'Heads: {percentage_heads}%')

# ===== My Version REFACTORED as per instructor ==== 

while True:
    user_choice = input('Throw the coin and enter head or tail here: ? ').lower().strip()
    if user_choice == 'q':
        break
    else:
        with open('./heads_or_tails/headstails.txt' , 'r') as file:
            users_past_choices = file.readlines()
            # needs to be readlines to ensure it is a LIST!!!!! -> Want to get seperate strings for each line

        users_past_choices.append(f'{user_choice}\n')

        with open('./heads_or_tails/headstails.txt' , 'a') as file:
            file.writelines(users_past_choices)
            # Needs to be writelines as it is writing a LIST!!!!!

        percentage_heads = (users_past_choices.count('head\n') / len(users_past_choices)) * 100
        print(f'Heads: {percentage_heads}%')


# ======== INSTRUCTORS VERSION ============

while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()
    
    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)
    # print(sides)
    
    # Valuable learning - take the count from instances in the list and compare with the length of the list 
    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")


        




