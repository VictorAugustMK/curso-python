"""
For loop

Loop -> Repetition structure.
For -> One of the repetition structures

C or Java

for(int i = 0; i < limit; i++) {
    //loop execution
}

Python

for i in iterable:
    //loop execution

We use loops to iterate over sequences or over iterable values

Examples of iterables:
- String
nanme = "Python Course"
- List
list = [1, 3, 5, 7, 9]
- Range
num = range(1, 10)
"""

# Examples iterating over a String
for i in name:
    print(i)

# Examples iterating over a List
for number in list:
    print(number)

# Examples iterating over a Range
for number in num:
    print(number)

# Examples for
name = "Curso Python"
list = [1, 3, 5, 7, 9]
num = range(1, 10) # Transform to list

for i, v in enumerate(name):
    print(name[i])

for i, v in enumerate(name):
    print(v)

for _, v in enumerate(name):
    print(v)

qnt = int(input("How many times should this loop run? "))

sum = 0

for n in range(1, qnt + 1):
    num = int(input(f"Inform the {n}/{qnt} value: "))
    sum = sum + num
print(f"The sum is {soma}")

name = "Curso Python"
for i in name:
    print(i, end=" ")
