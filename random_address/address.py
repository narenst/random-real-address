from .state import State


class Address:
    street1: str
    street2: str
    city: str
    state: str
    zip_code: str
    state_abbreviation: State

    def __init__(self, street1, street2, city, state, zip_code):
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.state_abbreviation = State.from_string(state)

    def __str__(self):
        return (
            f"{self.street1}\n{self.street2}\n{self.city}, {self.state} {self.zip_code}"
        )

    def __eq__(self, other):
        return (
            self.street1 == other.street1
            and self.street2 == other.street2
            and self.city == other.city
            and self.state == other.state
            and self.zip_code == other.zip_code
        )
