# Random Real Address Generator

![PyPI Version](https://img.shields.io/pypi/v/random-real-address)

Generate random, realistic addresses from a curated list. This Python library allows you to obtain random addresses or addresses specific to any U.S. state. It includes a collection of actual addresses that provide realistic data points for testing or demonstration purposes.

## Features

- Generate random addresses across the U.S.
- Generate random addresses specific to a U.S. state
- Provides structured data (street, city, state, zipcode)
- Incorporates official state abbreviations

## Installation

You can install the package via pip:

```
pip install random-address-generator
```

## Usage

### Generating a Random Address

```py
from from random_address import generate_random_address
print(generate_random_address())

Output:

```bash
208 Northwind Dr

Goodlettsville, Tennessee 37072
```

### Generating an Address in a Specific State

```py
from random_address import generate_random_address_in_state, State
print(generate_random_address_in_state(State.CA))
print(generate_random_address_in_state(State.ME))
```

Output:

```bash
1839 Arbor Way
Turlock, California 95380

10 Bass Ln
Winterport, Maine 04496
```

## Learn More

For more details, visit the project page on PyPI: [Random Real Address on PyPI](https://pypi.org/project/random-real-address/)

## Development

To develop on this repository use `bin/install` to set up your environment. And run `bin/test` to run tests.

## Contributing

Feel free to contribute by submitting pull requests or reporting issues.

1. Fork the project.
2. Make your feature addition or bug fix.
3. Add tests for your changes.
4. Ensure all tests are passing.
5. Submit a pull request.

## License

This project is licensed under the MIT License.


