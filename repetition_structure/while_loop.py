"""
While Loop

General form

while boolean_expression:
    //loop execution

The while block will be repeated while the boolean expression is true.

A boolean expression is any expression where the result is true or false.
"""
# Example:

num = 5
num < 5 (False)
num < 10 (True)

# Example 1
num = 1
while num < 10:
    print(num)
    num = num + 1
# NOTE: In a while loop, it is important that we take care of the stopping criteria to avoid causing an infinite loop.

# Example 2
answord = ""
while answord != "yes":
    answord = input(f"It's over?\n")
