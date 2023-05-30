import datetime 

def greet():
    dt = datetime.datetime.now().strftime('%A %d %B %Y, %I:%M%p')
    if dt[-2:] == "AM":
        time_greet = "Good Morning"
    elif dt[-2:] == "PM":
        time_greet = "Good Afternoon"
    print(f"\n{time_greet}. It is {dt}.\n")


# print(f"Todays date: {dt}")
if __name__ == "__main__":
    greet()