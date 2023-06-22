import configparser

def get_unit(question):
    # Dictionary is ordered by unit length and value shows multiple
    parser = configparser.ConfigParser()
    parser.read("units.ini")
    units = parser._sections["Units"]

    weight_error = "Input must be a valid measurement of weight"
    boundary_error = "Unit must be higher than 0"

    while True:
        try:
            user_input = input(question)
            # Loop through the units to find what was given
            for unit in units:
                length = len(unit)
                if (user_input[-length:]).lower() == unit.lower():
                    # Seperate the number from the unit
                    num = user_input[:-length]
                    if float(num) > 0:
                        # Makes sure the unit has a proper value
                        if num == "":
                            raise ValueError(weight_error)
                        user_number = float(num)
                    else:
                        raise ValueError(boundary_error)

                    return user_number * float(units[unit])
            raise ValueError(weight_error)
        except ValueError as error:
            print(error)