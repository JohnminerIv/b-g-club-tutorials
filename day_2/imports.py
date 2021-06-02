# day_2/imports.py
"""
Imports are normally included at the top of your file. When you import a file
everything in it is executed, but it also gives you access to the functions or
classes from that file. We'll go over classes next class.

In order to run this file with absolute imports you will need to run

python3 -m day_2.imports

Run that command from b-g-club-tutorials/
"""
# This is a standard library import 
import random

# this is an import of module you would need to install
# if you want this import to work run 'python3 -m pip install flask' in your terminal
# from flask import Flask


# this is a relative import, it imports using a relative path
from .functions import add_5_and_6

# these are absolute imports, they import using an absolute path
import day_2.functions as f
import day_2.if_main as if_main
from day_2.parameters import everything as e




if __name__ == '__main__':
    print('')
    print('*' * 80)
    print('Everything that happened above the *s is a side effect of not using if mains in the other files.')
    print('')
    print(random.random())

    print('-' * 80)
    print(add_5_and_6())

    print('-' * 80)
    f.recursive_function(7)

    print('-' * 80)
    print(if_main.example_function()) # this only prints hello, not hello main bcause it is not the main file.

    print('-' * 80)
    print(e(1,2,3,4, z=9))


