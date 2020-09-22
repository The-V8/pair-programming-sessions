#!/usr/bin/env bash

# This is an example of a test
# Run the tests with: bats my_test.sh

@test "Test Description" {
  run bash my_script.sh InputVariable
  (( status == 0 ))
  [[ $output == "Expected Output" ]]
}
