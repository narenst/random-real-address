from csv import DictReader
from random import choice

from .address import Address
from .state import State


def generate_random_address() -> Address:
    """
    Returns a random US address.
    Parses the address from the addresses.csv file in the root directory.
    """
    with open("addresses.csv") as file:
        addresses = list(DictReader(file))

    random_address = choice(addresses)
    return Address(
        street1=random_address["street1"],
        street2=random_address["street2"],
        city=random_address["city"],
        state=random_address["state"],
        zip_code=random_address["zipcode"],
    )


def generate_random_address_in_state(state: State) -> Address | None:
    """
    Returns a random US address in the given state.
    """
    with open("addresses.csv") as file:
        addresses = list(DictReader(file))

    addresses_in_state = [
        address for address in addresses if address["state"] == state.value
    ]
    if not addresses_in_state:
        return None

    random_address = choice(addresses_in_state)
    return Address(
        street1=random_address["street1"],
        street2=random_address["street2"],
        city=random_address["city"],
        state=random_address["state"],
        zip_code=random_address["zipcode"],
    )
