import unittest
from pytest import mark

from random_address import (
    generate_random_address,
    generate_random_address_in_state,
    Address,
    State,
)


def test_generate_random_address():
    address = generate_random_address()
    assert isinstance(address, Address)
    assert address.street1 is not None
    assert address.city is not None
    assert address.state is not None
    assert address.zip_code is not None
    assert address.state_abbreviation is not None


def test_addresses_are_unique():
    address1 = generate_random_address()
    address2 = generate_random_address()
    assert address1 != address2


def test_generate_random_address_in_state():
    address = generate_random_address_in_state(State.CA)
    assert address.street1 is not None
    assert address.city is not None
    assert address.state is not None
    assert address.zip_code is not None
    assert address.state_abbreviation is not None


@mark.parametrize(
    "state",
    [state for state in State],
)
def test_random_address_for_every_state(state: State):
    address = generate_random_address_in_state(state)
    assert address is not None
