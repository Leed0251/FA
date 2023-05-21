def not_blank(question):
    user_input = input(question)
    # Check if blank
    if user_input == "":
        print("Input can not be blank")
        user_input = not_blank(question)
    return user_input

def replace_blank(question, default):
    user_input = input(question)
    # Check if blank
    if user_input == "":
        # Replace user response with default
        user_input = default
        return user_input, True

    return user_input, False

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