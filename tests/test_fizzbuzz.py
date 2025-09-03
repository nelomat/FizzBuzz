import pytest
from fizzbuzz import is_divisible_by, generate_fizzbuzz

def test_is_divisible_by_known_words():
    assert is_divisible_by(15, "Fizz") is True
    assert is_divisible_by(10, "Buzz") is True
    assert is_divisible_by(7, "Fizz") is False

def test_is_divisible_by_unknown_word():
    with pytest.raises(ValueError):
        is_divisible_by(10, "Bazz")  # 'Bazz' is not defined in RULES

def test_generate_fizzbuzz_classic():
    out = generate_fizzbuzz(1, 15)
    assert out[2] == "Fizz"      # 3
    assert out[4] == "Buzz"      # 5
    assert out[14] == "FizzBuzz" # 15

def test_generate_fizzbuzz_range_validation():
    with pytest.raises(ValueError):
        generate_fizzbuzz(10, 1)