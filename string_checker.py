def not_blank(question, default):
    user_input = input("\x1B[0m" + question + "\x1B[35m")
    # Check if blank
    if user_input == "":
        if default == None:
            print("\x1B[31mInput can not be blank")
            user_input = not_blank(question, default)
        else:
            # Replace input, and return value
            user_input = default
            return user_input, True
    # Return user input
    if default:
        # Return with second value False if there was a default value
        return user_input, False
    return user_input

def yes_no(question):
    # All possible yes, no responses
    responses = ["yes", "no"]

    # Loop until input is valid
    valid = False
    while not valid:

        response = input("\x1B[0m" + question + "\x1B[34m").lower()

        if response != "":
            # Check if responses contain use input
            for item in responses:
                if response in item:
                    return item
            print("\x1B[31mInput must be 'yes' or 'no'")
        else:
            print("\x1B[31mInput can not be blank")