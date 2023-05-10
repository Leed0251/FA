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