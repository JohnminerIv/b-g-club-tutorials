# day_2/functions.py

"""
So far we have been writing everything in what is called a global scope. That is
fine for learning about coding and very simple programs, but it can lead to
spaghetti code in longer projects so today were going to start making our own
functions. Don't worry, you have already used functions before.
"""

# ▽ print is a function
print('Hello')
#        ^ It takes an argument between it's parentheses and tries to print it to the terminal

"""
So how can we make our own function? We start by defining the function, then
calling it.
"""

# The def key word allow us to define a new function with a new name, the
# parentheses would contain any arguments the function needs
def my_basic_function():
    pass # Pass is a key word that allows us to define a function that doesn't have any code in it yet.

"""
Now how would we call this function? We would do it as shown below.
"""

my_basic_function()

"""
Functions can be used to return values, we do this with the return keyword.
"""

def add_5_and_6():
    return 5 + 6

eleven = add_5_and_6() # the function is executed and the value that is returned is assigned to the variable
print(eleven)

"""
We can even call a function from another function. Or use global variable that
has already been assigned. It is highly dicouraged to use global variables for
most things this is simply for demonstrative purposes.
"""

def call_another_function():
    return add_5_and_6() + 2 + eleven

print(call_another_function())


"""
You can even call a function from within itself, that is called recursion. It
can be used like a loop and is very usedful for solving some problems. We might
talk about this more if some of you are interested.
"""

def recursive_function(call_count: int=0):
    if call_count != 10:
        print(f'Recusive fuction called {call_count, "-" * call_count}')
        recursive_function(call_count + 1)
        print(f'Recusive fuction finish {call_count, "-" * call_count}')

recursive_function()



