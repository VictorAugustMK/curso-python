
"""
Logical Structures: and, or, not, is

Unary operators:
    - not

Binary operators:
    - and, or, is

Operating rules:

For 'and', both values need to be True
For 'or', either value must be True.
For 'not', the boolean value is inverted, that is, if it is True, it becomes False, if it is False it becomes True
"""

active = True
logged_in = True

#Logical Structures AND
if active and logged_in:
    print("Welcome User!")
else:
    print("You need to activate your account, please check your e-mail")
#Logical Structures OR
if active or logged_in:
    print("Welcome User!")
else:
    print("You need to activate your account, please check your e-mail")
#Logical Structures NOT
if not active:
    print("You need to activate your account, please check your e-mail")
else:
    print("Welcome User!")
##Logical Structures IS
if active:
    print("You need to activate your account, please check your e-mail")
else:
    print("Welcome User!")