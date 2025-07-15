"""
List

Lists in Python work like arrays in other languages, with the difference that they are DYNAMIC
and can also contain ANY type of data.

C/Java languages: Arrays
- They have a fixed size and data type:
That is, in these languages, if you create an int array with size 5, this array will ALWAYS be an integer
and can ALWAYS contain a maximum of 5 values.

In Python:
- Dynamic: They do not have a fixed size; That is, we can create the list and simply add elements;
- Any type of data: They do not have a fixed data type; That is, we can contain different types of data;

Lists in Python are represented by square brackets: []

"""

list0 = [1, 99, 4, 27, 14, 22, 3, 1, 44, 42, 27]
list1 = ["C", "u", "r", "s", "o", " " ,"P", "y", "t", "h", "o", "n"]
list2 = []
list3 = list(range(11))
list4 = list("Curso Python")

# We can easily check if a given value is in the list
num = 0
if num in list3:
    print(f"I found number {num}")
else:
    print(f"I not found number {num}")

# We can easily order the list
list0.sort()
print(list0)

# We can easily count the number of occurrences of one value in a list
print(list0.count(1))
print(list4.count("e"))

# Add elements in a list
# To add elements in lists we use the function "append"
# OBS: With "append" we only can do add 1 element at a time
print(list0)
list0.append(42)
print(list0)

#OBS: For add more then 1 element in a list we need to use a object list
list0.append([8, 3, 1]) # Add in list how element list(sublist)
print(list0)

if [8, 3, 1] in list0:
    print(f"I found list")
else:
    print(f"I not found list")

list0.extend([123, 44, 67]) # Add in list each element with addicinal value from the list
print(list0)

# We can insert a new element on the list informing the index position
list0.insert(2, "New Value")
print(list0)