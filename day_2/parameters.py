# day_2/parameters.py

"""
Remember how we could use a variable from outside of a function in our last
demonstration? We used a variable from the global scope in our function, which
isn't really the best way of giving our function information. This also means
that our function might unexpectedly make changes to the global variable.

I'll give you a demonstation of what I mean.
"""

age = 16

def age_plus_2():
    global age # We can use the global keyword to explicately access the global scope
    age = age + 2
    return age

print(age)
print(age_plus_2()) # Notice how we don't tell the function where to get the age value?
print(age) # Notice how this variable changed?

"""
Normally we don't want our functions to have these side effects because they can
become hard to keep track of and debug. What we want is for our functions to
return the value and then we can choose to change the global variable or not.
"""

age = 16 # reset age to 16

def better_age_plus_2(age):
    age = age + 2
    return age

print(age)
print(better_age_plus_2(age)) # Notice how we pass the age variable to the function now
print(age) # this variable doesn't change


"""
Now we can call this function on any number and its not relying on a global var
to find the number.
"""
print(better_age_plus_2(7)) 


"""
Functions are useful for doing the same thing in mutiple parts of your code. 
For example say you want to draw a box around a line you print to the terminal.
You could manually do it like this
"""

print("""-------
|Hello|
-------""")


print('-'*80)
"""
Or you could create a way to do that and just write it out every time you need to.
"""

print(f"""{'-' * (len('Hello') + 2)}
|{'Hello'}|
{'-' * (len('Hello') + 2)}""")

print(f"""{'-' * (len('There') + 2)}
|{'There'}|
{'-' * (len('There') + 2)}""")

print('-'*80)

"""
Thats realy difficult to do, and the point of coding is to make your life easier.
So lets make a function that can make this happen for us for any word that we give it.
"""

def box_it(string):
    dashes = '-' * (len(string) + 2)
    return '{}\n|{}|\n{}'.format(dashes, string, dashes)

print(box_it('hi'))
print(box_it('there'))

print('-'*80)


# or how about 

def box_list(ls):
    full_string = ''
    for word in ls:
        full_string += box_it(word) + '\n'
    return full_string


words_to_say = ['hi', 'there', 'everyone']
print(box_list(words_to_say))



"""
So far I have mostly demonstrated single, unamed parameter functions but you can
make function with multiple paramenters. Named parameters, other arguments and
other keyword arguments. Parameters can also have default values.
"""

def add_1(x, y):
    return x + y

print(add_1(1, 2))


def add_2(x, y=100):
    return x + y

print(add_2(2))  # y defualts to 100
print(add_2(7,6)) # sets y to 6 instead of 100

def add_3(x, *, y):
    return x + y

print(add_3(7, y=10)) # y is a named parameter so we have to say y=(some value)

def add_4(x, *numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_4(1, 2, 3, 4, 5)) # this is 14 because the first arg is assigned to x, but the remaining ones are all assigned to numbers

def add_5(**named_numbers):
    key_list = []
    total = 0
    for key, value in named_numbers.items():
        key_list.append(key)
        total += value
    return key_list, total

print(add_5(k=7, d=3, w=5))

print('-' * 80)

def everything(x, *args, z, y=10,**kwargs):
    output = ''
    output += 'x = ' + str(x) + '\n'
    for index, arg in enumerate(args):
        output += 'args at ' + str(index) + ' is: ' + str(arg) + '\n'
    output += 'z has no default and = ' + str(z) + '\n'
    output += 'y defualted to = ' + str(y) + '\n'
    for key, value in kwargs.items():
        output += 'kwargs at ' + str(key) + ' is: ' + str(value) + '\n'
    return output

print(everything(3,4,5,6,7,8, r=50, t=20, z=100))



        

