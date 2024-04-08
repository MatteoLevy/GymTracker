import pytest
from utils.InputsValidator import InputsValidator

input_validator = InputsValidator()


# Test Valid Input: ensure that the function returns the correct input when the user provides a valid choice.
def test_get_string_input_valid_choice():
    prompt = "Enter your choice: "
    user_input = "Y"

    # Simulate input() function
    def mock_input(_):
        return user_input

    # Patch input() function with mock_input
    with pytest.MonkeyPatch.context() as m:
        m.setattr("builtins.input", mock_input)
        result = input_validator.get_string_input(prompt, valid_choices=["Y", "N"])

    # Check the result
    assert result == "Y"


# Test Case Insensitivity: verify that the function is case-insensitive when checking valid choices.
def test_get_string_input_case_insensitive():
    prompt = "Enter your choice: "
    user_input = "n"

    def mock_input(_):
        return user_input

    with pytest.MonkeyPatch.context() as m:
        m.setattr("builtins.input", mock_input)
        result = input_validator.get_string_input(prompt, valid_choices=["Y", "N"])
    assert result == "N"


def test_get_string_input_invalid_then_valid():
    prompt = "Enter your choice: "
    user_inputs = ["maybe", "yes"]

    # Simulate input() function
    def mock_input(_):
        return user_inputs.pop(0)

    # Patch input() function with mock_input
    with pytest.MonkeyPatch.context() as m:
        m.setattr("builtins.input", mock_input)
        result = input_validator.get_string_input(prompt, valid_choices=["yes", "no"])

    # Check the result
    assert result == "YES"
