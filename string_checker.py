def string_checker(question):
    user_input = input(question)
    # Check if blank
    if user_input == "":
        print("Input can not be blank")
        user_input = string_checker(question)
    return user_input