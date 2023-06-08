import math

def num_checker(question, num_type):
    user_input = input(question)

    # Take user input and turn into number
    try:
        number_input = num_type(user_input)
        if number_input <= 0 or math.isnan(number_input):
            print("Input must be a number higher than 0")
            # Ask again if doesn't meet boundaries
            number_input = num_checker(question, num_type)
    except:
        # Ask again if string
        print("Input is not a valid number")
        number_input = num_checker(question, num_type)
    finally:
        # Return valid number
        return number_input