def not_blank(question, default):
    user_input = input(question)
    # Check if blank
    if user_input == "":
        if default == None:
            print("Input can not be blank")
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

        response = input(question).lower()

        if response != "":
            # Check if responses contain use input
            for item in responses:
                if response in item:
                    return item
            print("Input must be 'yes' or 'no'")
        else:
            print("Input can not be blank")