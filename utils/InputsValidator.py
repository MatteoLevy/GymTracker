class InputsValidator:
    def __init__(self):
        pass

    # Verify that the string input is among the valid choices, if any, and throws error otherwise and asks for input again.
    def get_string_input(self, prompt, valid_choices=None):
        while True:
            user_input = (
                input(prompt).strip().upper()
            )  # Strip leading and trailing whitespaces
            if valid_choices is None or user_input in map(str.upper, valid_choices):
                return user_input
            else:
                print(
                    f'Error! Value not allowed! Allowed choices: {", ".join(map(repr, valid_choices))}'
                )

    # Verify that the input is an integer, throws error otherwise and asks for input again.
    def get_integer_input(self, prompt):
        while True:
            try:
                user_input = input(prompt).strip()
                return int(user_input)
            except ValueError:
                print("Error! Insert an integer number (e.g. '8' or '12')")

    # Verify that the input is a number formatted as an int or a float or a comma-separated number,
    # throws error otherwise and asks for input again.
    def get_number_input(self, prompt):
        while True:
            try:
                user_input = input(prompt).strip()
                user_input = user_input.replace(
                    ",", "."
                )  # Replace comma, if present, with period
                return float(user_input)  # Attempt to convert to float
            except ValueError:
                print("Error! Insert a number (e.g. '20', '20.5', or '20,5')")
