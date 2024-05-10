from random_address import State


def test_state_from_string_valid():
    state = State.from_string("California")
    assert state == State.CA


def test_state_from_string_invalid():
    try:
        state = State.from_string("Invalid State")
        assert False  # This line should not be reached
    except ValueError as e:
        assert str(e) == "Invalid state: Invalid State"


def test_state_enum_uniqueness():
    values = [state.value for state in State]
    assert len(values) == len(set(values))
