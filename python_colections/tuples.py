"""
Tuples

Tuples are quite similar to lists.

There are two basic differences:

1 - Tuples are represented by parentheses ()

2 - Tuples are immutable: This means that once created, they cannot be changed. Any operation on a tuple
generates a new tuple.

# WARNING 1: Tuples are represented by (), but see:
tuple1 = (1, 2, 3, 4, 5, 6, 7)
print(tuple1)
print(type(tuple1))
print()

tuple2 = 1, 2, 3, 4, 5, 6, 7
print(tuple2)
print(type(tuple2))
print()

# WARNING 2: Tuples with 1 element:
tuple3 = (4) # This is not a tuple!
print(tuple3)
print(type(tuple3))

# CONCLUSION: We can conclude that tuples are defined by commas and not by the use of parentheses

(4) -> Not a tuple
(4,) -> Is a tuple
4,  -> Is a tuple

# We can generate a tuple dynamically with range(start, stop, step)
tuple1 = tuple(range(11))
print(tuple1)

# Tuple unpacking

course_info = ('Python Course', 'Python Programming: Essentials')
school, course = course_info

print(school)
print(course)

# NOTE: Will raise ValueError if the number of elements doesn't match for unpacking.

# Methods for adding and removing elements in tuples do not exist, as tuples are immutable.

# Sum*, Max Value*, Min Value* and Length

# * If the values are integers or floats.

numbers = (1, 2, 3, 4, 5, 6)
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(len(numbers))

# Tuple concatenation

tuple1 = (1, 2, 3)
print(tuple1)
tuple2 = (4, 5, 6)
print(tuple2)

print(tuple1 + tuple2) # Tuples are immutable

tuple3 = tuple1 + tuple2
print(tuple3)

tuple1 = tuple1 + tuple2 # Tuples are immutable, but we can overwrite the variable
print(tuple1)

# Check if an element exists in the tuple

numbers = (1, 2, 3)

print(3 in numbers)

# Iterating over a tuple

numbers = (1, 2, 3)

for n in numbers:
    print(n)

for index, value in enumerate(numbers):
    print(index, value)

# Counting elements in a tuple

letters = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(letters.count('a'))

school_name = tuple('Python Course',)
print(school_name)

print(school_name.count('C'))

# Accessing elements in a tuple is also similar to lists
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print(months[5])

# Iterating with While
i = 0
while i < len(months):
    print(months[i])
    i += 1

# Finding the index of an element in the tuple

print(months.index('June', 5))

# NOTE: If the element doesn't exist, a ValueError will be raised.

# Tips on using tuples
# We should ALWAYS use tuples when we don't need to modify the data in a collection

# Example 1

# Slicing

# tuple[start: stop: step]

print(months[5:9])

# Why use tuples?

# - Tuples are faster than lists.
# - Tuples make your code safer*.

# * Because working with immutable elements brings more safety to your code.

# Copying a tuple to another
original = (1, 2, 3)
print(original)

copy = original # With tuples, shallow copy is not a problem
print(copy)

another = (4, 5, 6)
copy = copy + another

print(copy)
"""
