from utils.InputsValidator import InputsValidator

input_validator = InputsValidator()


def test_get_number_input_valid_integer(monkeypatch):
    prompt = "Enter a number: "
    user_input = "12"

    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_number_input(prompt)
    assert result == 12


def test_get_number_input_valid_float(monkeypatch):
    prompt = "Enter a number: "
    user_input = "7.50"

    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_number_input(prompt)
    assert result == 7.50


def test_get_number_input_valid_comma_separator(monkeypatch):
    prompt = "Enter a number: "
    user_input = "22,5"

    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_number_input(prompt)
    assert result == 22.5


def test_get_number_input_invalid(monkeypatch, capsys):
    prompt = "Enter a number: "
    user_inputs = ["three", "3"]

    def mock_input(_):
        return user_inputs.pop(0)

    monkeypatch.setattr("builtins.input", mock_input)

    input_validator.get_number_input(prompt)

    captured = capsys.readouterr()
    assert "Error! Insert a number" in captured.out


def test_get_number_input_whitespaces_input(monkeypatch):
    prompt = "Enter a number: "
    user_input = "   15   "

    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = input_validator.get_number_input(prompt)
    assert result == 15
