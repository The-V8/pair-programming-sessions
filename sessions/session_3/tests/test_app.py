from app import get_aliquot_sum


PERFECT_NUMBERS = [6, 28, 496]
ABUNDANT_NUMBERS = [12, 24]
DEFICIENT_NUMBERS = [5, 7, 13, 23]


def test_placeholder():
    assert True


def test_perfect_numbers():
    # TODO: Finish this test
    for number in PERFECT_NUMBERS:
        assert get_aliquot_sum(number)


# TODO: Add a test for abundant numbers

# TODO: Add a test for deficient numbers
