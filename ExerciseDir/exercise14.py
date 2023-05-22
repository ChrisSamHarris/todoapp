# Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature. 
# In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid" as a string depending on the temperature. 

gas_temp = 100
solid_temp = 0

def element_state(temp, sol=solid_temp, gas=gas_temp):
    if temp > 100:
        state = "gas"
    elif sol < temp < gas:
        state = "water"
    else:
        state = "solid"

    return state

temperature = float(input('What is the temperature of the water? '))
print(element_state(temperature))

# In coding exercise 1, we hardcoded the values 0 and 100. It is better to change them to constants in the script where the function is defined.
#  Therefore, your task is to modify the script from exercise 1 by creating two global variables/constants in that file, one variable associated with 0 and another associated with 100.
#  Then, use those variables in the function instead of the values.