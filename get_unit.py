import configparser
from itertools import groupby

def get_unit(question):
    # Convert units to grams or mililitres
    # Code from https://blog.finxter.com/how-to-split-a-string-between-numbers-and-letters/
    parser = configparser.ConfigParser()
    parser.read("units.ini")
    units = parser._sections["Units"]

    weight_error = "Input must be a valid measurement of weight"
    boundary_error = "Unit must be higher than 0"

    while True:
        try:
            user_input = input(question)
            split = ["".join(g) for _, g in groupby(user_input, str.isalpha)]

            if len(split) != 2:
                raise ValueError(weight_error)

            value = float(split[0])
            unit = split[1].lower()

            if unit in units:
                unit_value = float(units[unit])
                returning = unit_value * value
                if 1 > returning:
                    raise ValueError(boundary_error)

                return unit_value * value

            raise ValueError(weight_error)
        except ValueError as error:
            print(error)
