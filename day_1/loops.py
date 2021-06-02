# day_1/loops.py
import random

"""
Loops are a way of executing the same block of code more than once. Loops can be
broken down into different categories. Ones where we know how many iterations we
need (or can find out), and ones where we don't know how many iterations we
need. This corresponds to two types of loops in python for loops and while loops. 
"""


"""
The first type of loops, the ones where you know how many iterations you need,
are a little simpler to understand so lets start there.
"""

# This will loop through the numbers from 0 to 9 and print them.
for number in range(10):
    print(f'This is iteration {number}')


animals = ['Cat', 'Dog', 'Goldfish', 'Pig', "Chicken"] # Creating a list of animals

# This will loop through the list of animals and print them
for animal in animals:
    print(f'A {animal} is a animal')


# This will find the length of the animals list and make a range of numbers that we can use to index.
for index in range(len(animals)):
    print(f'The {animals[index]} is at index {index}.')

print('-----------------------------------------------------------------------')

"""
While loops are a little bit more difficult to work with because they can have
some unexpected consequenses. They can also continue looping forever if you
don't give the correct conditions. 
"""

number = 0
while number < 10: # as long as number is < 10 it'll keep looping
    print(f'This is iteration {number}')
    number += 1 # if we comment out this line what do you think will happen?


letters = 'abcdefghijklmnopqrstuvwxyz'
number = random.random()
fake_word = ''

while number < 0.9:
    fake_word += random.choice(letters)
    print(f'Our fake word is {fake_word} the number is {round(number, 2)}')
    number = random.random()

print(f'The word is {len(fake_word)} letters long')


