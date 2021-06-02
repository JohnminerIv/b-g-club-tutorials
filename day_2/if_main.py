# day_2/if_main.py

def example_function():
    string = 'Hello'
    if __name__ == '__main__':
        print('DEBUG: only want to see this debug if im running this file')
    return string


"""
If you check if the current script is the main script you can execute code in it
and not have to worry about it executing that code when you import it into other
files.
"""

if __name__ == '__main__':
    print(example_function())
