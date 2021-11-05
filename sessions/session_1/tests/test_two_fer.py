from sessions.session_1.two_fer import (
    two_fer_basic, two_fer_multiple, two_fer_multiple_assign
)


def test_two_fer_basic():
    name = "Natasha"
    actual = two_fer_basic(name)
    expected = "One for Natasha, one for me."

    assert actual == expected


def test_two_fer_multiple():
    name = "Wanda"
    amount = "ten"
    actual = two_fer_multiple(name, amount)
    expected = "Ten for Wanda, ten for me."

    assert actual == expected


def test_two_fer_multiple_assign():
    name = "Carol"
    share = ("five, four")
    actual = two_fer_multiple_assign(name, share)
    expected = "Five for Carol, four for me."

    assert actual == expected

# Stretch goal: Add more tests, especially for missing values :-)
