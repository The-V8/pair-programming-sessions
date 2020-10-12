from app import get_aliquot_sum


PERFECT_NUMBERS = [6, 28, 496]
ABUNDANT_NUMBERS = [12, 24]
DEFICIENT_NUMBERS = [5, 7, 13, 23]


def test_perfect_numbers():
    for num in PERFECT_NUMBERS:
        aliquot_sum = get_aliquot_sum(num)
        assert aliquot_sum == num, (
            f"number {num} is not equal to its aliquot sum {aliquot_sum}")


def test_abundant_numbers():
    for num in ABUNDANT_NUMBERS:
        aliquot_sum = get_aliquot_sum(num)
        assert aliquot_sum > num, (
            f"number {num} isn't smaller than its aliquot sum {aliquot_sum}")


def test_deficient_numbers():
    for num in DEFICIENT_NUMBERS:
        aliquot_sum = get_aliquot_sum(num)
        assert aliquot_sum < num, (
            f"number {num} isn't larger than its aliquot sum {aliquot_sum}")
