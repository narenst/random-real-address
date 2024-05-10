import unittest

from random_address import generate_random_address

class TestRandomAddress(unittest.TestCase):
    def test_generate_random_address(self):
        address = generate_random_address()
        self.assertTrue(isinstance(address, str))
        self.assertGreater(len(address), 0)