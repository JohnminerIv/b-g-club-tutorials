# day_3/tracebacks.py
from .classes import *
"""
We're going to walk through debuging this together.
"""


if __name__ == '__main__':
    student = create_student('John', '18', '12')

    print(student.introduce())
    student.get_older(23)
    print(introduce_student(student))

    person = Person('Cat', '6')
    student.add_friend(person)
    print(list_friends(student))

    print(list_friends(add_friend(person, person)))