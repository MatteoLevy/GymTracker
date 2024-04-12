from utils.InputsValidator import InputsValidator

input_validator = InputsValidator()


# Test Valid String Input: ensure that the function returns the correct string input when provided.
def test_get_string_input_valid_choice(monkeypatch):
    prompt = "Enter your choice: "
    user_input = "Y"

    # Patching input() function with a mock
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_string_input(prompt, valid_choices=["Y", "N"])
    assert result == "Y"


# Test Case Insensitive String Input: ensure that the function is case-insensitive when checking valid choices.
def test_get_string_input_case_insensitive(monkeypatch):
    prompt = "Enter your choice: "
    user_input = "n"

    # Patching input() function with a mock
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_string_input(prompt, valid_choices=["Y", "N"])
    assert result == "N"


# Test Invalid String Input: ensure that the function handles invalid string input and asks for input again.
def test_get_string_input_invalid_then_valid(monkeypatch, capsys):
    prompt = "Enter your choice: "
    user_inputs = ["maybe", "yes"]

    # Patching input() function with a mock that returns different values on each call
    def mock_input(_):
        return user_inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)

    result = input_validator.get_string_input(prompt, valid_choices=["yes", "no"])

    # Check if the function prompts the user again
    captured = capsys.readouterr()
    assert "Error! Value not allowed" in captured.out

    # Check if the result is correct
    assert result == "YES"


# Test Empty String Input: ensure that the function handles empty string input correctly.
def test_get_string_input_empty_input(monkeypatch, capsys):
    prompt = "Enter your choice: "
    user_inputs = ["", "Y"]

    # Patching input() function with a mock that returns different values on each call
    def mock_input(_):
        return user_inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)

    result = input_validator.get_string_input(prompt, valid_choices=["Y", "N"])

    # Check if the function prompts the user again
    captured = capsys.readouterr()
    assert "Error! Value not allowed" in captured.out

    # Check if the result is correct
    assert result == "Y"


# Test String Input with Whitespaces: ensure that the function handles string input with leading and trailing whitespaces correctly.
def test_get_string_input_whitespaces_input(monkeypatch):
    prompt = "Enter your choice: "
    user_input = "   Y   "

    # Patching input() function with a mock
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_string_input(prompt, valid_choices=["Y", "N"])
    assert result == "Y"
