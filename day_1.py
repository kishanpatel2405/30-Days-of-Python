# ------ 1	Introduction of python

# it is used for web development
# software development
# mathematics,
# system scripting
# used to handle big data


# ------ 1	Python Syntax

# indentation in Python is very important.
# if you want to print hello world than only you can write
print('Hello World')
# write a variable using only (variable is a name for storage)
a = 'kishan'
b = 90
# it is right syntax for comparing to variable
if a == b:
    print('a is same as b')
else:
    print('a is not as b')
# it will give the error because indentation is not right
# if 5 > 2:
# print("Five is greater than two!")


# ------ 1	Python Comments

# two types of comment
# 1- single line comment using # key word
# 2- multiline comment using """multiline string (triple quotes) also multiline string(single quotes)"""
# ex
# this is single line comment
"""This
    is
    multiline
    comment"""


# ------ 1	Python Docstring

# it is used for readability and maintainability
# example
# Functional docstring
def fun(parameter):
    """
    This function is parameterized function
    This is a function
    """
    pass


# class docstring
class name:
    """
    This is a class.
    """

    def __init__(self):
        """
        This is a constructor.
        """
        pass

    pass
    

# Module docstring
"""
This is a Module Docstring.
"""
