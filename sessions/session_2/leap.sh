#!/usr/bin/env bash
my_script() {   
    echo "Expected Output."
}

my_script "$@"



# You have to write the leap year functionality  in 3 iterations:

# 1. Leap year, if number is divisible by 4 (e.g. 2004 - yes, 1986 - no)

# 2. Leap year, if number is divisible by 4 and not by 100 (e.g. 2008 - yes, 2100 - no)

# 3. Leap year, if number is divisible by 4 and not by 100, 
#    but if divisible by 100, then also a leap year, if divisible by 400 (e.g. 2000 - yes, 1900 - no)
