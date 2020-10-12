# Challenge 3

## Application description

Our application should be able to check, if a number is perfect, abundant or deficient.

1. Perfect number:
    - A number is perfect, if the sum of the factors of a number (not including the number itself) - also called **aliquot sum** - is equal the actual number.
    - E.g. (6 = 1 + 2 + 3) or (28 = 1 + 2 + 4 + 7 + 14)
1. Abundant:
    - A number is abundant, if their aliquot sum is higher than the actual number.
    - E.g. (12 < 16 = 1 + 2 + 3 + 4 + 6) or (24 < 36 = 1 + 2 + 3 + 4 + 6 + 8 + 12)
1. Deficient:
    - A number is deficient, if their aliquot sum is lower than the actual number.
    - e.g. all prime numbers, as their aliquot sum is always 1

## Running the application

Run the application and tests before by building and running the docker image.

The tests will run, when the container is built, through the Makefile.

The application will run after the *docker run* command.

```bash
cd sessions/session_3/
docker build -t python-pairing-app:0.1 .
docker run -it --rm python-pairing-app:0.1
```

## Challenge 3 - Acceptance criteria

- Write a program in Python that implements the perfect number test functionality
- Test the given example behavior by writing Python tests in the **/tests** directory
  - make sure to write tests into the **test_app.py** file begin each method name with: **test_**
  - an example is given in the **test_app.py** file ( **def test_placeholder()** )
- You solved the problem with the [strong style pairing](https://martinfowler.com/articles/on-pair-programming.html#Strong-stylePairing) approach to pair programming
