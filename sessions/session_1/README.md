# Challenge 1

`Two-fer` or `2-fer` is short for two for one. One for you and one for me.

Given a name, return a string with the message:

```text
One for name, one for me.
```

Where "name" is the given name.

However, if the name is missing, return the string:

```text
One for you, one for me.
```

Here are some examples:

|Name      |String to return
|:---------|:------------------
|Alexander |One for Alice, one for me.
|Oliver    |One for Oliver, one for me.
|          |One for you, one for me.
|Peter     |One for Peter, one for me.

Run the tests with [Bats](https://github.com/bats-core/bats-core#installation)

```bash
bats my_test.sh
```

## Acceptance criteria

- Write a program in bash that implements the Two-Fer functionality
- Test the given example behavior with bats
- You solved the problem with the driver/navigator approach to pair programming
