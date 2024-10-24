# 15	Python Error Types

# 15	Syntax Error

# >>> print 'hello'
#   File "<stdin>", line 1
#     print 'hello'
#     ^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>>


# 15	Name Error

# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'age' is not defined
# >>>


# 15	Index Error

# >>> l = [1,2,3,4,5,6,7]
# >>> l[10]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>>


# 15	Module Not Found Error

# >>> import ls
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'ls'
# >>> import os
# >>>


# 15	Attribute Error

# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
# >>> math.pi
# 3.141592653589793
# >>>


# 15	Key Error

# >>> d = {'name' : 'kishan', 'age' : 21}
# >>> d['name']
# 'kishan'
# >>> d['ge']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'ge'


# 15	Type Error

# >>> 12 + '12'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>>


# 15	Import Error

# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math' (unknown location)
# >>> from math import pow
# >>>


# 15	Value Error

# >>> int('21a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '21a'
# >>>


# 15	Zero Division Error

# >>> 1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>>
