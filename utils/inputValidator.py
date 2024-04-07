# Verify that the string input is among the valid choices, if any, and throws error otherwise and asks for input again.
def get_string_input(prompt, valid_choices=None):
    while True:
        user_input = input(prompt).upper()
        if valid_choices is None or user_input in map(str.upper, valid_choices):
            return user_input
        else:
            print(
                f'Error! Value not allowed! Allowed choices: {", ".join(map(repr, valid_choices))}'
            )


# Verify that the reps input is an integer, throws error otherwise and asks for input again.
def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Error! Insert an integer number (e.g. '8' or '12')")
