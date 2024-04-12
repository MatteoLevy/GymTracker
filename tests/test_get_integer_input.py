from utils.InputsValidator import InputsValidator

input_validator = InputsValidator()


# Test Valid Integer Input: ensure that the function returns the correct integer input when provided.
def test_get_integer_input_valid(monkeypatch):
    prompt = "Enter an integer: "
    user_input = "42"

    # Patching input() function with a mock
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_integer_input(prompt)
    assert result == 42


# Test Invalid Integer Input: ensure that the function handles invalid integer input and asks for input again.
def test_get_integer_input_invalid_then_valid(monkeypatch):
    prompt = "Enter an integer: "
    user_inputs = ["not_an_integer", "42"]

    # Patching input() function with a mock that returns different values on each call
    def mock_input(_):
        return user_inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)

    result = input_validator.get_integer_input(prompt)
    assert result == 42


# Test Empty Input: ensure that the function handles empty input and asks for input again.
def test_get_integer_input_empty_input(monkeypatch, capsys):
    prompt = "Enter an integer: "
    user_inputs = ["", "42"]

    # Patching input() function with a mock that returns different values on each call
    def mock_input(_):
        return user_inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)

    result = input_validator.get_integer_input(prompt)

    # Check if the function prompts the user again
    captured = capsys.readouterr()
    assert "Error! Insert an integer number" in captured.out

    # Check if the result is correct
    assert result == 42


# Test Negative Integer Input: ensure that the function handles negative integer input correctly.
def test_get_integer_input_negative_input(monkeypatch):
    prompt = "Enter an integer: "
    user_input = "-42"

    # Patching input() function with a mock
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_integer_input(prompt)
    assert result == -42


# Test Zero Input: ensure that the function handles zero input correctly.
def test_get_integer_input_zero_input(monkeypatch):
    prompt = "Enter an integer: "
    user_input = "0"

    # Patching input() function with a mock
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_integer_input(prompt)
    assert result == 0


# Test Input with Leading and Trailing Whitespaces: ensure that the function handles input with leading and trailing whitespaces correctly.
def test_get_integer_input_whitespaces_input(monkeypatch):
    prompt = "Enter an integer: "
    user_input = "  42  "

    # Patching input() function with a mock
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_integer_input(prompt)
    assert result == 42
