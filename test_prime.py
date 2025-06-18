"""Test File for prime.py"""

import pytest
from prime import generate_prime_factors

def test_invalid_input_types():
    with pytest.raises(ValueError):
        generate_prime_factors("invalid")
    with pytest.raises(ValueError):
        generate_prime_factors(-1.11)

def test_input_one():
    assert generate_prime_factors(1) == []

def test_factor_of_two():
    assert generate_prime_factors(2) == [2]

def test_factor_of_three():
    assert generate_prime_factors(3) == [3]

def test_factors_of_four():
    assert generate_prime_factors(4) == [2, 2]

def test_factors_of_six():
    assert generate_prime_factors(6) == [2, 3]

def test_factors_of_eight():
    assert generate_prime_factors(8) == [2, 2, 2]

def test_factors_of_nine():
    assert generate_prime_factors(9) == [3, 3]
