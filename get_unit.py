import configparser
from itertools import groupby

def get_unit(question):
    # Convert units to grams or mililitres
    # Code from https://blog.finxter.com/how-to-split-a-string-between-numbers-and-letters/
    parser = configparser.ConfigParser()
    parser.read("units.ini")
    units = parser._sections["Units"]

    weight_error = "\x1B[31mInput must be a valid measurement of weight\x1B[0m"
    boundary_error = "\x1B[31mThat looks like a typo, please try again\x1B[0m"

    while True:
        try:
            user_input = input("\x1B[0m" + question + "\x1B[32m")
            split = ["".join(g) for _, g in groupby(user_input, str.isalpha)]

            if len(split) != 2:
                raise ValueError(weight_error)

            value = float(split[0])
            unit = split[1].lower()

            if unit in units:
                unit_value = float(units[unit])
                returning = unit_value * value
                if returning > 5000 or returning < 1:
                    raise ValueError(boundary_error)

                return unit_value * value

            raise ValueError(weight_error)
        except ValueError as error:
            print(error)