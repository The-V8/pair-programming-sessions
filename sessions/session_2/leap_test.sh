#!/usr/bin/env bash

# This is an example of a test
# Run the tests with: bats leap.sh

# 
@test 'This is your test description' {
  # The following line can be used to skip a specific test if uncommented
  #[[ $BATS_RUN_SKIPPED == "true" ]] || skip
  run bash leap.sh YEAR

  (( status == 0 ))
  [[ $output == "false" ]]
}


# You have to write 6 tests in 3 iterations (for each iteration, one for true, one for false):

# 1. Check the leap year for a year that is: 
#    divisible by 4 (true - 1904, false - 1986)
# -> Support your pair until the test is green

# 2. Check the leap year for a year that is:
#    divisible by 4 and not by 100 (true - 2008, false - 2100)
# -> Support your pair until the test is green

# 3. Check the leap year for a year that is:
#    divisible by 4 and not by 100
#    but if divisible by 100, then also a leap year, if divisible by 400 
#    (true - 2000, false - 1900)
# -> Support your pair until the test is green

# 4. If you have the time, you can think of other checks, e.g. checking for the right input