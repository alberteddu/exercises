# -*- coding: utf-8 -*-
# Exercise 1
#
# (This is a comment)
#
# Write a function named "hello", that takes two parameters.
# name: name of the person to greet (string).
# times: how many times the function should greet 'name'.
#
# The function should write to stdout the following string:
#
#    'Hello, $name. '
#
# where $name is the variable (first parameter).
# If times is greater than 4, the name will not be repeated
# after the fourth greeting.
#
# Examples:
#
#     hello('Alberto', 1)
#
#   = 'Hello, Alberto. ' <--- Note there is a space after the dot.
#
#     hello('Alberto', 5)
#
#   = 'Hello, Alberto. Hello, Alberto. Hello, Alberto. Hello, Alberto. Hello. '
#
#

def hello(name, times):
    if times > 4:
        print "Hello, %s. " % name *4 + "Hello. " *(times-4)
    else:
        print "Hello, %s. " % name *(times)
        
def hello_better(name, times):
    print "Hello, %s. " % name * (4 if times > 4 else times) + "Hello. " * (times-4)
        
hello_better('Alberto', 10)
