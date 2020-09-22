# Challenge 2

Given a year, report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

- on every year that is evenly divisible by 4
- except every year that is evenly divisible by 100
- unless the year is also evenly divisible by 400

Examples:

- 1904 is a leap year
- 1986 is not a leap year
- 2008 is a leap year
- 2100 is not a leap year
- 2000 is a leap year
- 1900 is not a leap year

For a delightful, four minute explanation of the whole leap year phenomenon, go watch this [youtube video](https://www.youtube.com/watch?v=xX96xng7sAE)

Run the tests with:

```bash
bats leap_test.sh
```

## Challenge 2 - Acceptance criteria

- Write a program in bash that implements the Leap Year functionality
- Test the given example behavior with bats
- You solved the problem with the ping/pong approach to pair programming